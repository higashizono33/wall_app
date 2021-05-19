from django.views.generic import ListView
from .models import Message, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'home.html'
    ordering = '-created_at'
    paginate_by = 5
    login_url = 'index'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('-created_at')
        return context

def post_message(request):
    if request.method == 'POST':
        if len(request.POST['message']) < 15:
            return JsonResponse({'error': 'Please enter your message at least 15 charactors'})
        else:    
            new_message = Message.objects.create(user=request.user, content=request.POST['message'])
            html = render_to_string('partial/message.html', {'message': new_message}, request=request)
            return JsonResponse({'html': html})

def delete_message(request, message_id):
    if request.method == 'GET':
        message = get_object_or_404(Message, pk=message_id)
        message.delete()
    return JsonResponse({'delete': True})

def edit_message(request, message_id):
    if request.method == 'POST':
        if len(request.POST['message']) < 15:
            return JsonResponse({'error': 'Please enter your message at least 15 charactors'})
        else:
            message = get_object_or_404(Message, pk=message_id)
            message.content = request.POST['message']
            message.save()
            return JsonResponse({'message': message.content})

def post_comment(request, message_id):
    if request.method == 'POST':
        if len(request.POST['comment']) < 15:
            return JsonResponse({'error': 'Please enter your comment at least 15 charactors'})
        else:
            message = get_object_or_404(Message, pk=message_id)
            Comment.objects.create(message=message, user=request.user, content=request.POST['comment'])
            comments = Comment.objects.all().order_by('-created_at')
            html = render_to_string('partial/comment.html', {'comments': comments, 'message': message}, request=request)
            return JsonResponse({'html': html})

def delete_comment(request, comment_id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
    return JsonResponse({'delete': True})

def edit_comment(request, comment_id):
    if request.method == 'POST':
        if len(request.POST['comment']) < 15:
            return JsonResponse({'error': 'Please enter your comment at least 15 charactors'})
        else:
            comment = get_object_or_404(Comment, pk=comment_id)
            comment.content = request.POST['comment']
            comment.save()
            return JsonResponse({'comment': comment.content})
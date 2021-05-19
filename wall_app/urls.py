from django.http import request
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post_message', post_message, name='post_message'),
    path('post_comment/<int:message_id>', post_comment, name='post_comment'),
    path('delete_message/<int:message_id>', delete_message, name='delete_message'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
    path('edit_message/<int:message_id>', edit_message, name='edit_message'),
    path('edit_comment/<int:comment_id>', edit_comment, name='edit_comment'),
]
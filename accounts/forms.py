from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True, validators=[validators.MinLengthValidator(2, 'Please enter at least 2 charactors')])
    last_name = forms.CharField(max_length=50, required=True, validators=[validators.MinLengthValidator(2, 'Please enter at least 2 charactors')])
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(CustomUserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

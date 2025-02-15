from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from manager_app.models import Task

class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'required': 'Please enter your username.'}
        self.fields['email'].error_messages = {'required': 'Please enter your email address.'}
        self.fields['password1'].error_messages = {'required': 'Please enter your password.'}
        self.fields['password2'].error_messages = {'required': 'Please confirm your password.'}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title','content']





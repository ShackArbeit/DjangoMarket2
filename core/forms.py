from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
      class Meta:
            model=User
            fields = ('username', 'email', 'password1', 'password2')
      username=forms.CharField(widget=forms.TextInput(attrs={
             'placeholder': '您的用戶名稱',
             'class': 'w-full py-4 px-6 rounded-xl'
      }))
      email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': '您的電子信箱',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
      password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '您的密碼',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
      password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '請再重複您的密碼',
        'class': 'w-full py-4 px-6 rounded-xl '
    }))

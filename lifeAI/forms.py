from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'senha'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'usuário'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
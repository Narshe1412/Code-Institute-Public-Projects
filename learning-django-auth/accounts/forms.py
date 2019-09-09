from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget = forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget = forms.PasswordInput, label="Password Confirmation")
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password")
    
        if password1 != password2:
            raise forms.ValidationError("Passwords must match")
        
        return password2
        
    
        
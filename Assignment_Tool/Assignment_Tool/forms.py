from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput())
  def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data
  def login(self, request):
          username = self.cleaned_data.get('username')
          password = self.cleaned_data.get('password')
          user = authenticate(username=username, password=password)
          return user

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
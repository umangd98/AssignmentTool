from django import forms
from .models import Instructor
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 

class InstructorRegisterForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ('profile_pic','bio', 'instructor_id')

class UserUpdateForm(UserChangeForm):
  
  class Meta:
    model = User
    fields = ['username', 'email','first_name', 'last_name' ]

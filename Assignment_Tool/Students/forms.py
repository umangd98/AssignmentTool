from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from Instructors.forms import UserUpdateForm

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('profile_pic', 'student_id')


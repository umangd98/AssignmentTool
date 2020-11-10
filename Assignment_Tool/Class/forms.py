from django import forms
from .models import Class, Section
from Students.models import Student

class CreateClassForm(forms.ModelForm):
  class Meta:
    model = Class
    fields = ('name',)



class CreateSectionForm(forms.ModelForm):
  
  class Meta:
    model = Section
    fields = ['name',]
  
  # students = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple)



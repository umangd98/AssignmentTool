from django import forms
from .models import Instructor

class InstructorRegisterForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ('bio', 'instructor_id')
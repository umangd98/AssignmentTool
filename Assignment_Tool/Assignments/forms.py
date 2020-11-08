from django import forms
from .models import Assignment


class CreateAssignmentForm(forms.ModelForm):
  # deadline = forms.DateTimeField(widget=forms.DateTimeInput)
  class Meta:
    model = Assignment
    fields = ('title', 'deadline', 'description', 'assignment_pdf', 'input_test_cases', 'output_test_cases')


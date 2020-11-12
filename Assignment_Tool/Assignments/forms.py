from django import forms
from .models import Assignment, Sent_Assignment


class CreateAssignmentForm(forms.ModelForm):
  # deadline = forms.DateTimeField(widget=forms.DateTimeInput)
  class Meta:
    model = Assignment
    fields = ('title', 'deadline', 'description', 'assignment_pdf', 'input_test_cases', 'output_test_cases')

class SendAssignmentForm(forms.ModelForm):
  class Meta:
    model = Sent_Assignment
    fields = ('section',)
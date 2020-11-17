from .models import Submission, Grade
from django import forms


class SubmissionForm(forms.ModelForm):
  class Meta:
    model = Submission
    fields = ('submission_file',)

class GradeForm(forms.ModelForm):
  class Meta:
    model = Grade
    fields = ('remark', 'grade', )
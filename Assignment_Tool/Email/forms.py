from django import forms

class MailForm(forms.Form):
  sectionId = forms.CharField(max_length=10)
  assignmentId = forms.CharField(max_length=10)

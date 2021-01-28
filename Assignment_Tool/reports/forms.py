from django import forms

class NameForm(forms.Form):
  Assignmentitle = forms.CharField(label = 'Assignment Title',max_length=100)
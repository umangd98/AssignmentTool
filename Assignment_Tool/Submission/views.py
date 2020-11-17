from django.shortcuts import render, redirect
from .forms import SubmissionForm, GradeForm
from .models import Submission, Grade
from Assignments.models import Assignment, Sent_Assignment
# Create your views here.
def SubmitAssignment(request,id):
  assignment = Assignment.objects.get(id=id)
  student = request.user.student
  sent_assignments = Sent_Assignment.objects.filter(assignment=assignment)
  print("Sent Assignments of this assignment: ", sent_assignments)
  sent_assignment = None
  for section in student.section_set.all():
    for s in sent_assignments.all():
      if(section==s.section):
        sent_assignment = s
  print("Chosen entry for student ",sent_assignment)
  submission = Submission.objects.filter(sent_assignment=sent_assignment, student= student).first()
  print("Submission Instance: ", submission)
  form = SubmissionForm(instance=submission)
  if request.method == 'POST':
    form = SubmissionForm(request.POST, request.FILES, instance=submission)
    if form.is_valid():
      form.save()
    return redirect('/assignment/'+str(assignment.id))
  return render(request, 'submit_assignment.html', {'form':form, 'assignment': assignment, 'user': student})

def ViewSubmission(request, id):
  submission = Submission.objects.get(id=id)
  print('Submission: ', submission)
  grade = Grade.objects.filter(submission=submission)
  if grade:
    print(grade.first().grade, grade.first().remark)
    pass
  form = GradeForm(instance=grade.first())
  if request.method == 'POST':
    form = GradeForm(request.POST, instance=grade.first())
    if form.is_valid():
      grade = form.save(commit=False)
      grade.submission = submission
      grade.save()
      return redirect('/submit_assignment/view/'+str(id))
  context = {
    'submission': submission,
    'form': form,
    'grade': grade.first()
  }
  return render(request, 'view_submission.html', context)
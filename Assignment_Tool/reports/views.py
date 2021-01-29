from django.shortcuts import render,redirect
from django.http import HttpResponse
from Submission.models import Submission, Grade
from Assignments.models import Assignment, Sent_Assignment

# Create your views here.
def reports(request,id):
  assignment = Assignment.objects.get(id=id)
  group = request.user.groups.all()[0].name
  instructor_submissions_submitted = []
  instructor_submissions_not_submitted = []
  grade_list = []
  sent_assignments = assignment.sent_assignment_set.all()
  no_of_submitted = 0
  no_of_not_submitted = 0
  is_instructor = False
  if group == 'instructor':
    #send form
    is_instructor=True
  # elif group == 'student':
  #   return redirect('/student') 

    for submission in Submission.objects.all():
      for ss in sent_assignments:
        if submission.sent_assignment == ss:
          if submission.submission_file.name:
            instructor_submissions_submitted.append(submission)
            no_of_submitted += 1
            #submission = Submission.objects.get(id=id)
            print('Submission: ', submission)
            grade = Grade.objects.filter(submission=submission)
            if grade:
              grade_list.append(grade.first().grade)
              print(grade.first().grade, grade.first().remark)
              pass
          else:
            instructor_submissions_not_submitted.append(submission)
            no_of_not_submitted += 1
    print("instructor_submissions_submitted: ",instructor_submissions_submitted)
    print("instructor_submissions_not_submitted: ",instructor_submissions_not_submitted)
    pass
  print("Grade List: ", grade_list)
  context = {
    'assignment': assignment,
    'is_instructor': is_instructor, 
    'instructor_submissions_submitted':instructor_submissions_submitted,
    'instructor_submissions_not_submitted':instructor_submissions_not_submitted,
    'no_of_not_submitted' : no_of_not_submitted,
    'no_of_submitted' : no_of_submitted,
    'grade_list' : grade_list
  }

  return render(request, 'reports.html', context)

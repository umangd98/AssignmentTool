from django.shortcuts import render, redirect
from .forms import CreateAssignmentForm, SendAssignmentForm
from django.http import HttpResponse
from .models import Assignment, Sent_Assignment
from Submission.models import Submission
from Class.models import Section
# Create your views here.

def create_assignment(request):
  if request.method == 'POST':
    form_assignment = CreateAssignmentForm(request.POST,request.FILES)
    if form_assignment.is_valid():
      instructor = request.user.instructor
      if instructor is not None:
        assignment = form_assignment.save(commit=False)
        assignment.instructor = instructor
        assignment.save()
        return HttpResponse('Assignment save is successful')
      else:
        return HttpResponse('Assignment save failed. Please check credentials')

  else:
    form1 = CreateAssignmentForm()
    

  return render(request, 'assignment_create.html', {'form1':form1, })

def view_assignment(request, id):
  assignment = Assignment.objects.get(id=id)
  group = request.user.groups.all()[0].name
  sent_assignments = assignment.sent_assignment_set.all()
  sent_sections = []
  is_instructor = False
  is_student = False
  print("Sent assignments of this assignment ",sent_assignments )
  student_submitted = False
  submission = None
  for s in sent_assignments:
    sent_sections.append(s.section)
  # print(sent_sections)
  instructor_submissions_submitted = []
  instructor_submissions_not_submitted = []
  if group == 'instructor':
    #send form
    is_instructor=True
   

    for submission in Submission.objects.all():
      for ss in sent_assignments:
        if submission.sent_assignment == ss:
          if submission.submission_file.name:
            instructor_submissions_submitted.append(submission)
          else:
            instructor_submissions_not_submitted.append(submission)
    print("instructor_submissions_submitted: ",instructor_submissions_submitted)
    print("instructor_submissions_not_submitted: ",instructor_submissions_not_submitted)
    pass
  elif group == 'student':
    #submission form
    is_student=True
    student = request.user.student
    submissions = student.submission_set.all()
    print("Submissions: ",submissions)
    for submission in submissions:
      if submission.sent_assignment.assignment == assignment:
        if submission.submission_file.name:
          student_submitted = True
          print("Submitted",submission, submission.submission_file.name)
          break
        else:
          print("Not Submitted")
          student_submitted = False
    # sent_assignments = [x for x in submissions.sent_assignment.all()]
    pass
  print(student_submitted)
  context = {
    'assignment': assignment,
    'sent_sections': sent_sections,
    'is_instructor': is_instructor, 
    'is_student': is_student,
    'student_submitted':student_submitted,
    'submission': submission,
    'instructor_submissions_submitted':instructor_submissions_submitted,
    'instructor_submissions_not_submitted':instructor_submissions_not_submitted

  }
  return render(request, 'view_assignment.html', context)


def update_assignment(request,id):
  assignment = Assignment.objects.get(id=id)
  if request.method == 'POST':
    form_assignment = CreateAssignmentForm(request.POST,request.FILES, instance=assignment)
    if form_assignment.is_valid():
      # instructor = request.user.instructor
      assignment = form_assignment.save(commit=False)
      assignment.save()
      return HttpResponse('Assignment save is successful')
    else:
      return HttpResponse('Assignment save failed. Please check credentials')

  else:
    form1 = CreateAssignmentForm(instance=assignment)
    

  return render(request, 'assignment_create.html', {'form1':form1, })

#Util function
#creates an entry in submission table for each student in the section in send_assignment
def addStudentinSubmission(sent_assignment_id, section_id):
  sent_assignment = Sent_Assignment.objects.get(id=sent_assignment_id)
  section = Section.objects.get(id=section_id)
  print("In the method",section.name, sent_assignment)

  for student in section.students.all():
    Submission.objects.create(student = student, sent_assignment=sent_assignment)
  print('Saved in Submissions')

#find the sections of user which hasn't been sent this assignment
def findNotSentSections(assignment_id, request):
  assignment = Assignment.objects.get(id=assignment_id)
  sent_assignments = assignment.sent_assignment_set.all()
  sent_sections = []
  for s in sent_assignments:
    sent_sections.append(s.section)
  
  instructor = request.user.instructor
  classes = instructor.classes.all()
  sections = []
  for c in classes:
    for section in c.section_set.all(): 
      sections.append(section)
  
  not_sent_sections = []
  for section in sections:
    if not section in sent_sections:
      not_sent_sections.append(section)
  
  return assignment, not_sent_sections

def send_assignment(request, id):
  form = SendAssignmentForm()
  assignment, not_sent_sections = findNotSentSections(id, request)
  print(not_sent_sections)
  if request.method == 'POST':
    form = SendAssignmentForm(request.POST)
    if form.is_valid():
      sent_assignment = form.save(commit=False)
      sent_assignment.assignment = assignment
      sent_assignment.save()

      print("Current Selected Section: ", sent_assignment.section,sent_assignment.id)

      addStudentinSubmission(sent_assignment.id, sent_assignment.section.id)
      return redirect('/assignment/' + str(assignment.id))
    else:
      return HttpResponse('Send_Assignment form is invalid')  


  return render(request, 'send_assignment.html', {'form':form, 'assignment': assignment, 'sections':not_sent_sections})

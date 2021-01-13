from django.shortcuts import render, redirect
from .forms import MailForm
from Class.models import Section
from Assignments.models import Assignment
from django.core.mail import send_mail

# Create your views here.

def sendMailAux(studentEmails, assignment):
  print('sending mail...')
  subject = assignment.title
  body = 'You have an assignment ' + assignment.title + 'deadline ' + str(assignment.deadline )+ 'Link ' + assignment.assignment_pdf.url
  from_mail = 'technopreneur123@gmail.com'
  retval = send_mail(subject, body, from_mail, studentEmails)
  if retval ==1:
    print('sent succesfull')

def send_email(request):
  # print(request.POST)
  studentEmails = []
  if request.method=='POST':
    form = MailForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      section = Section.objects.get(pk=cd['sectionId'])
      assignment = Assignment.objects.get(pk=cd['assignmentId'])
      class_name = section.class_name
      for student in section.students.all():
        studentEmails.append(student.user.email)
      assignmentURL = assignment.assignment_pdf.url
      sendMailAux(studentEmails, assignment)
    # print(studentEmails, assignmentURL)

  # return redirect('/class/1/section/1')

  return redirect('/class/' + str(class_name.id) + '/section/' + str(section.id))
  
def send_email_grades(assignment, user, grade):
  print('sending mail...')
  subject = assignment.title + " " + grade.grade
  body = 'You have received grade for assignment ' + assignment.title + 'by  ' + str(assignment.instructor.user.get_full_name() )+ 'Remark: ' + grade.remark
  from_mail = 'technopreneur123@gmail.com'
  retval = send_mail(subject, body, from_mail, (user.email,))
  if retval ==1:
    print('sent succesfull')
from django.shortcuts import render
from .forms import InstructorRegisterForm, UserUpdateForm
from Assignment_Tool.forms import CreateUserForm
from django.http import HttpResponse
from Assignment_Tool.decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def home(request):
  instructor = request.user.instructor
  assignments = instructor.assignment_set.all()
  classes = instructor.classes.all()
  context = {
    'assignments': assignments,
    'classes': classes
  }
  return render(request, 'home_instructor.html', context)


@unauthenticated_user
def instructor_register(request):
  if request.method == 'POST':
    form_user = CreateUserForm(request.POST)
    form_instructor = InstructorRegisterForm(request.POST,request.FILES)
    if form_user.is_valid() and form_instructor.is_valid():
      user = form_user.save()
      if user is not None:
        instructor = form_instructor.save(commit=False)
        instructor.user = user
        group = Group.objects.get(name='instructor')
        user.groups.add(group)
        instructor.save()
        return HttpResponse('Instructor save is successful')
      else:
        return HttpResponse('Instructor save failed. Please check credentials')

  else:
    form1 = CreateUserForm()
    form2 = InstructorRegisterForm()

  return render(request, 'register.html', {'form1':form1, 'form2':form2})

@login_required(login_url='/login/')
def instructor_update(request):
  if request.method == 'POST':
    form_user = UserUpdateForm(request.POST, instance=request.user)
    form_instructor = InstructorRegisterForm(request.POST, request.FILES, instance=request.user.instructor)
    if form_user.is_valid() and form_instructor.is_valid():
      user = form_user.save()
      instructor = form_instructor.save()
      return HttpResponse('Instructor save is successful')
  else:
    form1 = UserUpdateForm(instance=request.user)
    form2 = InstructorRegisterForm(instance=request.user.instructor)

  return render(request, 'register.html', {'form1':form1, 'form2':form2, 'title': 'Update'})
from django.shortcuts import render
from .forms import InstructorRegisterForm
from Assignment_Tool.forms import CreateUserForm
from django.http import HttpResponse
from Assignment_Tool.decorators import unauthenticated_user
from django.contrib.auth.models import Group

# Create your views here.

@unauthenticated_user
def instructor_register(request):
  if request.method == 'POST':
    form_user = CreateUserForm(request.POST)
    form_instructor = InstructorRegisterForm(request.POST)
    if form_user.is_valid() and form_instructor.is_valid():
      user = form_user.save()
      # user = authenticate(request, username=cd['username'], password=cd['password'])
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
  
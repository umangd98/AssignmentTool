from django.shortcuts import render
from .forms import StudentRegisterForm, UserUpdateForm
from Assignment_Tool.forms import CreateUserForm
from django.http import HttpResponse
from Assignment_Tool.decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from Submission.models import Submission

# Create your views here.


def home(request):
    student = request.user.student
    assignments = student.submission_set.all()
    print(assignments)
    context = {
      'assignments': assignments
    }
    return render(request, 'home_student.html', context)


# @unauthenticated_user
# def student_register(request):
#     if request.method == 'POST':
#         form_user = CreateUserForm(request.POST)
#         form_student = StudentRegisterForm(request.POST)
#         if form_user.is_valid() and form_student.is_valid():
#             user = form_user.save()
#             if user is not None:
#                 student = form_student.save(commit=False)
#                 student.user = user
#                 group = Group.objects.get(name='student')
#                 user.groups.add(group)
#                 student.save()
#                 return HttpResponse('Student save is successful')
#             else:
#                 return HttpResponse('Student save failed. Please check credentials')

#     else:
#         form1 = CreateUserForm()
#         form2 = StudentRegisterForm()

#     return render(request, 'register_student.html', {'form1': form1, 'form2': form2, 'title': 'Student'})

@unauthenticated_user
def student_register(request):
  if request.method == 'POST':
    form_user = CreateUserForm(request.POST)
    form_student = StudentRegisterForm(request.POST)
    print(form_user.is_valid(),form_user.errors, form_student.is_valid())
    if form_user.is_valid() and form_student.is_valid():
      user = form_user.save()
      if user is not None:
        student = form_student.save(commit=False)
        student.user = user
        group = Group.objects.get(name='student')
        user.groups.add(group)
        student.save()
        return HttpResponse('Student save is successful')
      else:
        return HttpResponse('Student save failed. Please check credentials')

  else:
    form1 = CreateUserForm()
    form2 = StudentRegisterForm()

  return render(request, 'register_student.html', {'form1':form1, 'form2':form2, 'title' : 'Student'})

@login_required(login_url='/login/')
def student_update(request):
    if request.method == 'POST':
        form_user = UserUpdateForm(request.POST, instance=request.user)
        form_student = StudentRegisterForm(
            request.POST, request.FILES, instance=request.user.student)
        if form_user.is_valid() and form_student.is_valid():
            user = form_user.save()
            student = form_student.save()
            return HttpResponse('Student save is successful')
    else:
        form1 = UserUpdateForm(instance=request.user)
        form2 = StudentRegisterForm(instance=request.user.student)

    return render(request, 'register_student.html', {'form1': form1, 'form2': form2, 'title': 'Update'})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user


@unauthenticated_user
def login_user(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'], password=cd['password'])
      if user is not None:
        login(request, user)
        # return HttpResponse('Auth is successful')
        group = request.user.groups.all()[0].name
        if group == 'instructor':
          # return instructor_update(request)
          return redirect('/instructor/')
          # return render(request, 'home.html', {'bio':user.instructor.bio})
        elif group == 'student':
          return redirect('/student/')
      else:
        return HttpResponse('Auth failed. Please check credentials')
  
  else:
    form = LoginForm()

  return render(request, 'login.html', {'form':form})


def home(request):
  return render(request, 'home.html')
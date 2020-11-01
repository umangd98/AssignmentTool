from django.shortcuts import render
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
        if user.instructor is not None:
          return render(request, 'home.html', {'bio':user.instructor.bio})
      else:
        return HttpResponse('Auth failed. Please check credentials')
  
  else:
    form = LoginForm()

  return render(request, 'login.html', {'form':form})


def home(request):
  return render(request, 'home.html')
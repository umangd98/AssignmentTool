from django.shortcuts import render
from .forms import CreateAssignmentForm
from django.http import HttpResponse
from .models import Assignment
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
  context = {
    'assignment': assignment
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
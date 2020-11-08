from django.shortcuts import render, redirect
from .forms import CreateClassForm, CreateSectionForm
from django.http import HttpResponse
from .models import Class, Section
# Create your views here.
def create_class(request):
  if request.method == 'POST':
    form_class = CreateClassForm(request.POST)
    if form_class.is_valid():
      instructor = request.user.instructor
      if instructor is not None:
        Class = form_class.save()
        instructor.classes.add(Class)
        instructor.save()
        return HttpResponse('Class Saved')
      else: 
        return HttpResponse('Class not saved')
  
  else:
    form1 = CreateClassForm()
  
  return render(request, 'create_class.html', {'form1':form1})


def view_class(request, id):
  class_name = Class.objects.get(id=id)
  if request.method == 'POST':
    form_section = CreateSectionForm(request.POST)
    if form_section.is_valid():
      section = form_section.save(commit=False)
      section.class_name = class_name
      section.save()
      form_section.save_m2m()

      return redirect('/class/'+str(class_name.id))
  sections = class_name.section_set.all()
  form_section = CreateSectionForm()
  context = {
    'class_name': class_name,
    'sections': sections,
    'form': form_section
  }
  return render(request, 'view_class.html', context)

def view_section(request, id, sid):
  class_name = Class.objects.get(id=id)
  # print(class_name.name)
  section = Section.objects.get(id=sid)
  students = section.students.all()
  if request.method == 'POST':
    form_section = CreateSectionForm(request.POST, instance=section)
    if form_section.is_valid():
      # instructor = request.user.instructor
      section = form_section.save(commit=False)
      # print('POST: ',request.POST)
      # print('section: ',section.students.all())
      # print(section.students.all())
      section.save()
      form_section.save_m2m()
      return redirect('/class/' + str(id) + '/section/' + str(sid))
    else:
      return HttpResponse('Assignment save failed. Please check credentials')
  form = CreateSectionForm(instance=section)
  context = {
    'class_name': class_name,
    'section': section,
    'students': students,
    'form': form
  }
  return render(request, 'view_section.html', context)

from django.db import models
from Students.models import Student
# Create your models here.



class Class(models.Model):
  name = models.CharField(max_length=30)
  created = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  class Meta: 
    verbose_name = "Class"
    verbose_name_plural = "Classes"

  def __str__(self):
      return self.name
  
class Section(models.Model):
  name = models.CharField(max_length=20)
  students = models.ManyToManyField(Student)
  created = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  class_name = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)
  def __str__(self):
      return self.name
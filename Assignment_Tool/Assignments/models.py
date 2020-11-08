from django.db import models
from Instructors.models import Instructor
# Create your models here.
def assignment_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'assignment_{0}/{1}'.format(instance.instructor.user.username, filename)

def input_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'assignment_input_{0}/{1}'.format(instance.instructor.user.username, filename)

def output_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'assignment_output_{0}/{1}'.format(instance.instructor.user.username, filename)

class Assignment(models.Model):
  title = models.CharField(max_length=100)
  deadline = models.DateTimeField()
  created = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  description = models.TextField()
  instructor = models.ForeignKey(Instructor, on_delete = models.CASCADE)
  assignment_pdf = models.FileField(upload_to=assignment_directory_path, null=True, blank=True)
  input_test_cases = models.FileField(upload_to=input_directory_path, null=True, blank=True)
  output_test_cases = models.FileField(upload_to=output_directory_path, null=True, blank=True)

  def __str__(self):
      return self.title
  

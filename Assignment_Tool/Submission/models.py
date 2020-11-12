from django.db import models
from Assignments.models import Sent_Assignment
from Students.models import Student

def submission_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'submission_{0}/{1}'.format(instance.student.user.username, filename)
# Create your models here.
class Submission(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  sent_assignment = models.ForeignKey(Sent_Assignment, on_delete=models.CASCADE)
  submitted = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  submission_file = models.FileField(upload_to=submission_directory_path, null=True, blank=True)

  def __str__(self):
      return self.student.user.username + " - " + self.sent_assignment.assignment.title
  


class Grade(models.Model):
  submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
  remark = models.CharField(max_length=200)
  grade = models.CharField(max_length=10)

  def __str__(self):
      return self.submission
  

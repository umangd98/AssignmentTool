from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    student_id = models.CharField(max_length=10)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
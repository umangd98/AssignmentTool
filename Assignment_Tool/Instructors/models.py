from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    bio = models.TextField(max_length=500, blank=True)
    instructor_id = models.CharField(max_length=20)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def create_user_instructor(sender, instance, created, **kwargs):
#     if created:
#         Instructor.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_instructor(sender, instance, **kwargs):
#     instance.instructor.save()
from django.urls import path, include
# from .views import login_user, home
from .views import student_register, home, student_update


urlpatterns = [
    path('', home, name='home_student'),
    path('register/', student_register, name='register_student'),
    path('update/', student_update, name='update_student')


]
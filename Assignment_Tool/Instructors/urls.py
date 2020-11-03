from django.urls import path, include
# from .views import login_user, home
from .views import instructor_register, home, instructor_update


urlpatterns = [
    path('', home, name='home_instructor'),
    path('register/', instructor_register, name='register_instructor'),
    path('update/', instructor_update, name='update_instructor')


]
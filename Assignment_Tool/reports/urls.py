from django.urls import path, include
# from .views import login_user, home
from .views import reportAssignment


urlpatterns = [
    path('', reportAssignment, name='reports')
]
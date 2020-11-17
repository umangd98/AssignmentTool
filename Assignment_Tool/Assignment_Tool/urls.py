"""Assignment_Tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import login_user, home

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_user, name='login_custom'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('instructor/', include('Instructors.urls')),
    path('student/', include('Students.urls')),
    path('assignment/', include('Assignments.urls')),
    path('class/', include('Class.urls')),
    path('submit_assignment/', include('Submission.urls')),



    # path('register_instructor/', instructor_register, name='register_instructor')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

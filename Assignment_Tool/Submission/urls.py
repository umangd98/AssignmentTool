from django.urls import path, include
from .views import SubmitAssignment,ViewSubmission


urlpatterns = [

     path('<int:id>/', SubmitAssignment, name='submit_assignment'),
     path('view/<int:id>/', ViewSubmission, name='view_submission'),


]
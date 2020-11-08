from django.urls import path, include
# from .views import login_user, home
from .views import create_assignment,view_assignment, update_assignment


urlpatterns = [
    # path('', home, name='view_assignments'),
    path('create/', create_assignment, name='create_assignment'),
    path('update/<int:id>', update_assignment, name='update_assignment'),
    # path('delete/', create_assignment, name='update_assignment'),
    path('<int:id>/', view_assignment, name='view_assignment'),


]
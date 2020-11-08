from django.urls import path, include
# from .views import login_user, home
from .views import create_class, view_class, view_section


urlpatterns = [
    # path('', home, name='view_assignments'),
    path('create/', create_class, name='create_class'),
    # path('update/<int:id>', update_assignment, name='update_assignment'),
    # # path('delete/', create_assignment, name='update_assignment'),
    path('<int:id>/', view_class, name='view_class'),
    path('<int:id>/section/<int:sid>/', view_section, name='view_section'),



]
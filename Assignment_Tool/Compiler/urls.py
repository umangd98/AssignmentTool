from django.urls import path
# from .views import login_user, home
from .views import index_compiler, run_compiler, run_check

urlpatterns = [
    path('', index_compiler, name='index_compiler'),
    path('run/', run_compiler, name='run_compiler'),
    path('run_check/', run_check, name='run_check'),

]
from django.urls import path
# from .views import login_user, home
from .views import index_compiler, run_compiler

urlpatterns = [
    path('', index_compiler, name='index_compiler'),
    path('run/', run_compiler, name='run_compiler'),
]
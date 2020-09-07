from django.urls import path, include
from . import views

urlpatterns = [
    path('manager/login', views.manager_login, name="manager_login"),
    path('employee/login', views.employee_login, name='employee_login'),
    path('employee/register', views.employee_registeration, name='employee_register'),
    path('manager/register', views.manager_registeration, name='manager_register'),
    path('admin/login', views.admin_login, name='admin_login'),
    path('admin/register', views.admin_registeration, name='admin_registration'),
    path('logout', views.sign_out, name='logout'),

]
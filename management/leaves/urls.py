from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.application_create, name='application_create'),
    path('list/', views.application_list, name='application_list'),
    path('<int:pk>/status/', views.application_status, name='aplication_status'),
    path('available/leaves/', views.available_leaves, name='available_leaves'),
    path('get/all/', views.track_applications, name='track_applications'),

]
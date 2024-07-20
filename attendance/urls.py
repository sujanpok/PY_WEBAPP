from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]

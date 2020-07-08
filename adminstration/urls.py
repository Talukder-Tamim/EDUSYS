from django.urls import path
from .import views

urlpatterns = [
    path('create', views.create_employee, name="create-employee"),
    path('list', views.employeeList, name="employee-list")
    ]
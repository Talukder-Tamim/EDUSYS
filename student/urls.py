from django.urls import path
from .import views

urlpatterns = [
    path('create', views.create_student, name="create-student"),
    path('list', views.student_list, name="student-list"),
    path('edit/<int:pk>', views.editStudentView, name="edit-student"),
    path('class/<class_name>', views.student_class, name="student-class"),
    path('register', views.registerView, name="register-student"),
    path('delete/<int:pk>', views.deleteStudentView, name="delete-student")
]
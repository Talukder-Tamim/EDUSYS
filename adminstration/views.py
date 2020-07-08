from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeCreateForm


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_obj = User.objects.create_user(username=username, password=password)
            new_user = form.save(commit=False)
            new_user.user = user_obj
            new_user.save()
            return redirect('home')
    else:
        form = EmployeeCreateForm()

    context = {'form': form}
    return render(request, 'adminstration/create employee.html', context)


def employeeList(request):
    employee = Employee.objects.all()
    context = {'employees': employee}
    return render(request, 'adminstration/employee_list.html', context)
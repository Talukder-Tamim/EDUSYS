from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import TeacherInfo
from .forms import TeacherForm

"""
def create_teacher(request):
    if request.method == "POST":
        forms = TeacherForm(request.POST)
        if forms.is_valid():
            t_name = forms.cleaned_data["name"]
            t_age = forms.cleaned_data["age"]
            t_gender = forms.cleaned_data["gender"]
            t_number = forms.cleaned_data["phone_number"]
            t_designation = forms.cleaned_data["designation"]
        TeacherInfo.objects.create(
            name = t_name,
            age = t_age,
            gender = t_gender,
            phone_number = t_number,
            designation = t_designation
        )
    forms = TeacherForm()
    context = {'forms': forms}
    return render(request, 'teacher/create_teacher.html', context)
"""

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_obj = User.objects.create_user(username=username, password=password)
            new_user = form.save(commit=False)
            new_user.user = user_obj
            new_user.save()
            return redirect('home')
    else:
        form = TeacherForm()

    context = {'forms': form}
    return render(request, 'teacher/create_teacher.html', context)


def teacher_list(request):
    teachers = TeacherInfo.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teacher/teacher_list.html', context)


def edit_teacher(request, teacher_id):
    teacher_obj = TeacherInfo.objects.get(id=teacher_id)
    forms = TeacherForm(instance=teacher_obj)
    if request.method=="POST":
        forms = TeacherForm(request.POST, instance=teacher_obj)
        if forms.is_valid:
            forms.save()
            return redirect('teacher-list')
    context = {'forms': forms}
    return render(request, 'teacher/edit_teacher.html', context)


def delete_teacher(request, teacher_id):
    teacher_obj = TeacherInfo.objects.get(id=teacher_id)
    teacher_obj.delete()
    return redirect('teacher-list')
    
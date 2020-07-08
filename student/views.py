from django.shortcuts import render, redirect
from .models import StudentDetailInfo, StudentInfo, StudentClassInfo
from .forms import StudentForm, StudentInfoForm, StudentDetailInfoForm 



def create_student(request):
    if request.method == "POST":
        forms = StudentForm(request.POST)
        if forms.is_valid():
            std_name = forms.cleaned_data["name"]
            std_age = forms.cleaned_data["age"]
            std_gender = forms.cleaned_data["gender"]
            std_roll = forms.cleaned_data["roll"]
            std_fathers = forms.cleaned_data["fathers_name"]
            std_address = forms.cleaned_data["address"]
            std_class = forms.cleaned_data["std_class"]
            std_shift = forms.cleaned_data["std_shift"]
            std_section = forms.cleaned_data["std_section"]
            std_session = forms.cleaned_data["std_session"]

            std_obj = StudentInfo.objects.create(
                name=std_name,
                age=std_age,
                roll=std_roll,
                fathers_name=std_fathers,
                gender=std_gender
                )
            StudentDetailInfo.objects.create(
                student=std_obj,
                std_class=std_class,
                std_shift=std_shift,
                std_section=std_section,
                std_session=std_session
                )
            return redirect('student-list')
    else:
        forms = StudentForm()   
    context = {'forms': forms}
    return render(request, 'student/create_std.html', context)



def registerView(request):
    form1 = StudentInfoForm(request.POST or None)
    form2 = StudentDetailInfoForm(request.POST or None)
    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():
            std_obj = form1.save()
            std_obj2 = form2.save(commit=False)
            std_obj2.student = std_obj
            std_obj2.save()
            return redirect('student-list')

    context = {'form1': form1, 'form2': form2}
    return render(request, 'student/register_std.html', context)


def student_list(request):
    students = StudentDetailInfo.objects.all()
    context = {'students': students}
    return render(request, 'student/student_list.html', context)


def editStudentView(request, pk):
    std_detail = StudentDetailInfo.objects.get(id=pk)
    std_info = std_detail.student

    form1 = StudentInfoForm(request.POST or None, instance=std_info)
    form2 = StudentDetailInfoForm(request.POST or None, instance=std_detail)

    if form1.is_valid() and form2.is_valid():
        std_obj = form1.save()
        std_obj2 = form2.save(commit=False)
        std_obj2.student = std_obj
        std_obj2.save()
        return redirect('student-list')
    
    context = {'form1': form1, 'form2': form2}
    return render(request, 'student/edit_student.html', context)


def deleteStudentView(request, pk):
    std_obj = StudentDetailInfo.objects.get(id=pk)
    std_obj.delete()
    return redirect('student-list')


def student_class(request, class_name):
    std_obj = StudentClassInfo.objects.filter(class_name=class_name)
    student = StudentDetailInfo.objects.filter(std_class=std_obj)
    context = {'students': student}
    return render(request, 'student/std_class.html', context)



    
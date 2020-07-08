from django import forms
from .models import StudentClassInfo, StudentShiftInfo, StudentInfo, StudentDetailInfo


class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = forms.ChoiceField(choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fathers_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    std_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all())
    std_shift = forms.ModelChoiceField(queryset=StudentShiftInfo.objects.all())
    std_section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    std_session = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'


class StudentDetailInfoForm(forms.ModelForm):
    class Meta:
        model = StudentDetailInfo
        exclude = ('student', )





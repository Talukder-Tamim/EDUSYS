from django import forms
from .models import TeacherInfo

"""

class TeacherForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = forms.ChoiceField(choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

"""

class TeacherForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = TeacherInfo
        fields = ('username', 'password', 'name', 'age', 'gender', 'phone_number', 'designation')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'})
        }


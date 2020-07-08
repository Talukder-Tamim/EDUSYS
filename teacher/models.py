from django.db import models


class TeacherInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(choices=gender_choice, max_length=6)
    phone_number = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name


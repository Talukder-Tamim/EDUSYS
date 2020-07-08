from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DESIGNATION = (
        ('accounts', 'Accounts'),
        )
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    designation = models.CharField(max_length=50, choices=DESIGNATION)

    def __str__(self):
        return self.name

# Generated by Django 3.0.7 on 2020-07-03 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_teacherinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherinfo',
            name='user',
        ),
    ]

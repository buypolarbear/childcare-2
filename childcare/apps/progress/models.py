from childcare.apps.membermanagement.models import Student
from django.contrib.auth.models import User
from django.db import models

class ActivityCategory(models.Model):

    name = models.CharField(max_length=100)


class Activity(models.Model):

    category = models.ForeignKey(ActivityCategory)
    teacher = models.ForeignKey(User)
    description = models.CharField(max_length=300)
    notes = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()




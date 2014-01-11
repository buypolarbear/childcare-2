from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    guardians = models.ManyToManyField(Guardian)
    birth_date = models.DateField()
    visits = models.ManyToManyField


class Guardian(AbstractBaseUser):

    joined_date = models.DateTimeField(auto_now_add=True)
    last_payment_date = models.DateField()
    payment_due_date = models.DateField()
    payment_schedule = models.IntegerField()
    billed_rate = models.DecimalField()


class Visit(models.Model):

    visit_start = models.DateTimeField()
    visit_end = models.DateTimeField()

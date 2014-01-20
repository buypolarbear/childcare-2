from django.contrib.auth.models import User
from django.db import models
import recurrence.fields

class Tenant(models.Model):

    name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=9)

class Visit(models.Model):

    visit_start = models.DateTimeField()
    visit_end = models.DateTimeField()


class Student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    visits = models.ManyToManyField(Visit)
    guardians = models.ManyToManyField(User)
    is_active = models.BooleanField()

class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True)
    tenant = models.ForeignKey(Tenant)

class PaymentDetails(models.Model):

    user = models.ForeignKey(User, unique = True)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_payment_date = models.DateField()
    payment_due_date = models.DateField()
    payment_schedule = models.IntegerField()
    billed_rate = models.DecimalField(decimal_places=2, max_digits=5)

class Note(models.Model):

    written_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=200)
    guardian = models.ForeignKey(User, related_name='Guardian')
    for_teacher = models.ForeignKey(User, related_name='For Teacher')
    student = models.ForeignKey(Student)
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField()
    recurrence = recurrence.fields.RecurrenceField()











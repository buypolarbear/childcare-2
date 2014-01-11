from apps.membermanagement.models import Student
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class StudentCreateView(ListCreateAPIView):
    model = Student


class StudentReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    model = Student

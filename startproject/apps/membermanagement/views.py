from django.contrib.auth.models import User
from models import Student, Note
from rest_framework import routers, viewsets


class StudentViewSet(viewsets.ModelViewSet):
    model = Student

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    model = User

class NoteViewSet(viewsets.ModelViewSet):
    model = Note




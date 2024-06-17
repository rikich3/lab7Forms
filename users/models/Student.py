# users/models/student.py
from django.db import models
from courses.models import Course
from users.models import User

class Student(User):
    courses = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE, null=True, blank=True)

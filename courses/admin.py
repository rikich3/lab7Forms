from django.contrib import admin
from courses.models import Course
from users.models import Student


# Register your models here.
admin.site.register(Course)
admin.site.register(Student)



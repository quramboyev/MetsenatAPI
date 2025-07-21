from django.contrib import admin
from .models import StudentModel, UniversityModel

admin.site.register(StudentModel)
admin.site.register(UniversityModel)
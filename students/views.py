from django.shortcuts import render
from .serializers import StudentModelSerializer, UniversityModel
from .models import *
from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
from django.shortcuts import render
from .serializers import StudentModelSerializer, UniversityModelSerializer
from .models import *
from rest_framework.viewsets import ModelViewSet
from config.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import StudentFilter, UniversityFilter

class StudentViewSet(ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentFilter

class UniversityViewSet(ModelViewSet):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversityModelSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = UniversityFilter
from django.shortcuts import render
from .models import SponsorModel, SponsorToStudentModel
from .serializers import SponsorModelSerializer, SponsorToStudentModelSerializer
from rest_framework.viewsets import ModelViewSet

class SponsorViewSet(ModelViewSet):
    queryset = SponsorModel.objects.all().order_by('created_at')
    serializer_class = SponsorModelSerializer

class SponsorToStudentViewSet(ModelViewSet):
    queryset = SponsorToStudentModel.objects.all()
    serializer_class = SponsorToStudentModelSerializer

from django.shortcuts import render
from .models import SponsorModel, SponsorToStudentModel
from .serializers import SponsorModelSerializer, SponsorToStudentModelSerializer
from rest_framework.viewsets import ModelViewSet
from config.permissions import IsAdminOrReadOnly

class SponsorViewSet(ModelViewSet):
    queryset = SponsorModel.objects.all().order_by('created_at')
    serializer_class = SponsorModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class SponsorToStudentViewSet(ModelViewSet):
    queryset = SponsorToStudentModel.objects.all()
    serializer_class = SponsorToStudentModelSerializer
    permission_classes = [IsAdminOrReadOnly]

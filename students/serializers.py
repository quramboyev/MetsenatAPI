from rest_framework import serializers
from .models import StudentModel, UniversityModel

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


class UniversityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = '__all__'



from rest_framework import serializers
from .models import SponsorModel, SponsorToStudentModel

class SponsorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = '__all__'

    def validate(self, data):
        sponsor_type = data.get('sponsor_type')

        if sponsor_type == SponsorModel.LEGAL and not data.get('organization_name'):
            raise serializers.ValidationError({
                'organization_name': 'Название организации обязательно для юридического лица.'
            })

        if sponsor_type == SponsorModel.PHYSICAL:
            data['organization_name'] = None

        return data


class SponsorToStudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorToStudentModel
        fields = '__all__'

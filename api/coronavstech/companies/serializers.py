from rest_framework import serializers
from .models import Companies


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = [
            'id',
            'name',
            'status',
            'application_link',
            'last_updated',
            'notes',
        ]

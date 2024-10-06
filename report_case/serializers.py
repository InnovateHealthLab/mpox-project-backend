from .models import NewCase
from rest_framework import serializers


class FillNewCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCase
        fields = '__all__'

class GetAllCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCase
        fields = '__all__'

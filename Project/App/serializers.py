from rest_framework import serializers
from .models import Hospital,HospitalFacilities
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class HospitalFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalFacilities
        fields = '__all__'



from rest_framework import serializers
from .models import Prescription, PrescriptionMedication, Medication


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class PrescriptionMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionMedication
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    medications = PrescriptionMedicationSerializer(many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = '__all__'

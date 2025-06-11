from rest_framework import serializers
from .models import Prescription, Medication


class MedicationSerializer(serializers.ModelSerializer):
    prescription = serializers.PrimaryKeyRelatedField(
        queryset=Prescription.objects.all(), required=True)
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Medication
        fields = '__all__'
        read_only_fields = ['created_at']



class PrescriptionSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(read_only=True)  # prevent override
    prescribed_date = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    status = serializers.ChoiceField(
        choices=Prescription.STATUS_CHOICES, default='active')

    class Meta:
        model = Prescription
        fields = '__all__'
        read_only_fields = ['doctor', 'prescribed_date', 'created_at']




from rest_framework import serializers
from .models import (
    Patient, EmergencyContact, Visit,
    Allergy, PatientAllergy,
    ChronicDisease, PatientChronicDisease,
    Surgery, PatientSurgery,
    Disability, PatientDisability,
    PatientMedication
)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class PatientAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAllergy
        fields = '__all__'


class PatientChronicDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientChronicDisease
        fields = '__all__'


class PatientSurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSurgery
        fields = '__all__'


class PatientDisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDisability
        fields = '__all__'


class PatientMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedication
        fields = '__all__'

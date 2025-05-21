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
        read_only_fields = ['patient']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
        read_only_fields = ['patient']


class PatientAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAllergy
        fields = '__all__'
        read_only_fields = ['patient']


class PatientChronicDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientChronicDisease
        fields = '__all__'
        read_only_fields = ['patient']


class PatientSurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSurgery
        fields = '__all__'
        read_only_fields = ['patient']


class PatientDisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDisability
        fields = '__all__'
        read_only_fields = ['patient']


class PatientMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedication
        fields = '__all__'
        read_only_fields = ['patient']


class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'


class ChronicDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChronicDisease
        fields = '__all__'


class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgery
        fields = '__all__'


class DisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disability
        fields = '__all__'

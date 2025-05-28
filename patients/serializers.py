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
        read_only_fields = ['user']  


class EmergencyContactSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EmergencyContact
        fields = '__all__'
        read_only_fields = ['patient']


class VisitSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Visit
        fields = '__all__'
        read_only_fields = ['patient']


class PatientAllergySerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(read_only=True)
    allergy_name = serializers.SerializerMethodField()
    class Meta:
        model = PatientAllergy
        fields = '__all__'
        read_only_fields = ['patient']

    def get_allergy_name(self, obj):
        return str(obj.allergy)


class PatientChronicDiseaseSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(read_only=True)
    disease_name = serializers.SerializerMethodField()
    class Meta:
        model = PatientChronicDisease
        fields = '__all__'
        read_only_fields = ['patient']

    def get_disease_name(self, obj):
        return str(obj.disease)


class PatientSurgerySerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(read_only=True)
    surgery_name = serializers.SerializerMethodField()
    class Meta:
        model = PatientSurgery
        fields = '__all__'
        read_only_fields = ['patient']

    def get_surgery_name(self, obj):
        return str(obj.surgery)
    
class PatientDisabilitySerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(read_only=True)
    disability_name = serializers.SerializerMethodField()
    class Meta:
        model = PatientDisability
        fields = '__all__'
        read_only_fields = ['patient']

    def get_disability_name(self, obj):
        return str(obj.disability)
    

class PatientMedicationSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(read_only=True)
    medication_name = serializers.SerializerMethodField()
    class Meta:
        model = PatientMedication
        fields = '__all__'
        read_only_fields = ['patient']
        
    def get_medication_name(self, obj):
        return str(obj.medication)


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

from django.contrib import admin
from .models import (
    Patient,
    EmergencyContact,
    Visit,
    PatientAllergy,
    PatientChronicDisease,
    PatientSurgery,
    PatientDisability,
    PatientMedication
)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',
                    'gender', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('gender',)


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('patient', 'name', 'relationship', 'phone_number')
    search_fields = ('name', 'relationship')
    list_filter = ('relationship',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('patient', 'visit_date', 'reason', 'doctor_name')
    search_fields = ('reason', 'doctor_name')
    list_filter = ('visit_date',)


@admin.register(PatientAllergy)
class PatientAllergyAdmin(admin.ModelAdmin):
    list_display = ('patient', 'allergy_name', 'severity')
    search_fields = ('allergy_name',)
    list_filter = ('severity',)


@admin.register(PatientChronicDisease)
class PatientChronicDiseaseAdmin(admin.ModelAdmin):
    list_display = ('patient', 'disease_name', 'diagnosis_date')
    search_fields = ('disease_name',)
    list_filter = ('diagnosis_date',)


@admin.register(PatientSurgery)
class PatientSurgeryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'surgery_name', 'surgery_date')
    search_fields = ('surgery_name',)
    list_filter = ('surgery_date',)


@admin.register(PatientDisability)
class PatientDisabilityAdmin(admin.ModelAdmin):
    list_display = ('patient', 'disability_type', 'notes')
    search_fields = ('disability_type',)


@admin.register(PatientMedication)
class PatientMedicationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication_name', 'dosage', 'frequency')
    search_fields = ('medication_name',)

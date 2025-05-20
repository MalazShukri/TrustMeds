from django.contrib import admin
from .models import (
    Patient, EmergencyContact, Visit,
    PatientAllergy, PatientChronicDisease,
    PatientSurgery, PatientDisability, PatientMedication
)

# --- Patient ---

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number',
                    'email_address')  # 'email' -> 'email_address'
    search_fields = ('first_name', 'last_name', 'phone_number')


# --- Emergency Contact ---
@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    # 'phone_number' -> 'phone'
    list_display = ('id', 'name', 'relationship', 'phone')


# --- Patient Allergy ---
@admin.register(PatientAllergy)
class PatientAllergyAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'get_allergy_name', 'notes')
    search_fields = ('patient__first_name',)

    def get_allergy_name(self, obj):
        return obj.allergy.name
    get_allergy_name.short_description = 'Allergy'


# --- Patient Chronic Disease ---
@admin.register(PatientChronicDisease)
class PatientChronicDiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'get_disease_name', 'notes')

    def get_disease_name(self, obj):
        return obj.disease.name
    get_disease_name.short_description = 'Disease'


# --- Patient Surgery ---
@admin.register(PatientSurgery)
class PatientSurgeryAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'get_surgery_name', 'date', 'notes')
    list_filter = ('date',)

    def get_surgery_name(self, obj):
        return obj.surgery.name
    get_surgery_name.short_description = 'Surgery'


# --- Patient Disability ---
@admin.register(PatientDisability)
class PatientDisabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'get_disability_name', 'notes')

    def get_disability_name(self, obj):
        return obj.disability.name
    get_disability_name.short_description = 'Disability'


# --- Patient Medication ---
@admin.register(PatientMedication)
class PatientMedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'get_medication_name',
                    'dosage', 'frequency')

    def get_medication_name(self, obj):
        return obj.medication.name
    get_medication_name.short_description = 'Medication'


# --- Visit ---
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'visit_date',
                    'get_doctor_name', 'diagnosis')

    def get_doctor_name(self, obj):
        return obj.doctor.full_name if obj.doctor else "-"
    get_doctor_name.short_description = 'Doctor'

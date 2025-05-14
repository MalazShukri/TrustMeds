from django.contrib import admin
from .models import Prescription, PrescriptionMedication, Medication


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'prescribed_date',
                    'expiration_date', 'status')
    list_filter = ('status', 'prescribed_date')
    search_fields = ('notes',)
    date_hierarchy = 'prescribed_date'


@admin.register(PrescriptionMedication)
class PrescriptionMedicationAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'name_en', 'dosage', 'frequency_en')
    search_fields = ('name_en', 'frequency_en')
    list_filter = ('dosage',)


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

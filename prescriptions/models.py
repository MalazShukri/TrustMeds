from django.db import models


class Prescription(models.Model):
    doctor = models.ForeignKey(
        'doctors.Doctor', on_delete=models.CASCADE, related_name='prescriptions')
    patient = models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE, related_name='prescriptions')
    prescribed_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription #{self.id} for {self.patient.first_name} on {self.prescribed_date}"


class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(
        'Prescription', on_delete=models.CASCADE, related_name='medications')
    medication = models.ForeignKey(
        'Medication', on_delete=models.SET_NULL, null=True, blank=True)
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, null=True, blank=True)

    dosage = models.CharField(max_length=100)
    frequency_en = models.CharField(max_length=255)
    frequency_ar = models.CharField(max_length=255)
    instructions_en = models.TextField(null=True, blank=True)
    instructions_ar = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_en} ({self.dosage})"


class Medication(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

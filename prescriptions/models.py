from django.db import models


class Prescription(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('fulfilled', 'Fulfilled'),  # or 'completed', 'seen_by_pharmacy', etc.
    ]
    doctor = models.ForeignKey(
        'doctors.Doctor', on_delete=models.CASCADE, related_name='prescriptions')
    patient = models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE, related_name='prescriptions')
    prescribed_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription #{self.id} for {self.patient.full_name}"


class Medication(models.Model):
    prescription = models.ForeignKey(
        'Prescription', on_delete=models.CASCADE, related_name='medications')
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

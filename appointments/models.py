from django.db import models
from doctors.models import Doctor
from patients.models import Patient


class Appointment(models.Model):
    # STATUS_CHOICES = [
    #     ('pending', 'Pending'),
    #     ('approved', 'Approved'),
    #     ('rejected', 'Rejected'),
    #     ('cancelled', 'Cancelled'),
    #     ('completed', 'Completed'),
    # ]

    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    # status = models.CharField(
    #     max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-time']
        unique_together = ['doctor', 'date', 'time']  

    def __str__(self):
        return f"{self.date} {self.time} - Dr. {self.doctor.full_name()} with {self.patient.user.email}"

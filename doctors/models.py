from django.db import models


class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    # Basic Info
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    # Contact Info
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True, blank=True)
    address = models.TextField(blank=True)

    # Professional Info
    specialization = models.CharField(max_length=255)

    # Employment
    clinic_or_hospital = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Dr. {self.full_name} ({self.specialization})"

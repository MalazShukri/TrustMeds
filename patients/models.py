from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    user = models.OneToOneField(
        'accounts.User', on_delete=models.CASCADE, related_name='patient_profile')

    # Basic Info
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.DecimalField(
        max_digits=5, decimal_places=2,
        null=True, blank=True,
        help_text="Patient height in centimeters"
    )
    weight = models.DecimalField(
        max_digits=5, decimal_places=2,
        null=True, blank=True,
        help_text="Patient weight in kilograms"
    )
    phone_number = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    # Medical Info
    blood_type = models.CharField(
        max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True)
    family_history = models.TextField(blank=True)
    pregnancy_status = models.CharField(max_length=50, blank=True)

    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)

    def get_prescriptions(self):
        return self.prescriptions.all()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class EmergencyContact(models.Model):
    patient = models.OneToOneField(
        'patients.Patient', on_delete=models.CASCADE, related_name='emergency_contact')
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.relationship})"


class Visit(models.Model):
    patient = models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE, related_name='visits')
    doctor = models.ForeignKey(
        'doctors.Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    visit_date = models.DateTimeField()
    notes = models.TextField()
    diagnosis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Visit of {self.patient.first_name} on {self.visit_date.date()}"


class Allergy(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_ar = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return self.name


class PatientAllergy(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('severe', 'Severe'),
    ]

    patient = models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE, related_name='allergies')
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    severity = models.CharField(
        max_length=10, choices=SEVERITY_CHOICES, default='low')
    diagnosed_date = models.DateField(null=True, blank=True)
    reaction = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.first_name} - {self.allergy.name}"


class ChronicDisease(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('resolved', 'Resolved'),
        ('unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=255, unique=True)
    name_ar = models.CharField(max_length=255, unique=True, null=True)
    doctor = models.CharField(max_length=55, null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE,
        related_name='chronic_diseases'
    )

    def __str__(self):
        return f"{self.patient.first_name} - {self.name}"

    
    
class Surgery(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_ar = models.CharField(max_length=255, unique=True, null=True)
    provider = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    doctor = models.CharField(max_length=55, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE,
        related_name='surgeries'
    )

    def __str__(self):
        return f"{self.patient.first_name} - {self.name}"



class Disability(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_ar = models.CharField(max_length=255, unique=True, null=True)
    patient = models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE, related_name='disabilities')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.first_name} - {self.name}"

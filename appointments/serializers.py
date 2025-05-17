from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(
        source='doctor.full_name', read_only=True)
    patient_email = serializers.EmailField(
        source='patient.user.email', read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['status', 'created_at']

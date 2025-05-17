from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer
from doctors.models import Doctor
from patients.models import Patient
from django.shortcuts import get_object_or_404


class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_doctor:
            return Appointment.objects.filter(doctor__user=user)
        elif user.is_patient:
            return Appointment.objects.filter(patient__user=user)
        return Appointment.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_patient:
            serializer.save(patient=user.patient)
        elif user.is_doctor:
            serializer.save(doctor=user.doctor)


class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

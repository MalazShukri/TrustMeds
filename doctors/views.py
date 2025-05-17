from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Doctor, DoctorSchedule
from .serializers import DoctorSerializer, DoctorScheduleSerializer
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from patients.models import Patient
from patients.serializers import PatientSerializer


# === Permission for doctor-only access ===

class IsDoctorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_doctor', False)


class CreateDoctorProfileView(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateDoctorProfileView(generics.UpdateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

    def get_object(self):
        return get_object_or_404(Doctor, user=self.request.user)


# === /me — Doctor Full Profile View (profile + appointments + patients)

class DoctorFullProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

    def get(self, request):
        doctor = get_object_or_404(Doctor, user=request.user)
        appointments = Appointment.objects.filter(doctor=doctor)
        patients = Patient.objects.filter(
            appointments__doctor=doctor).distinct()

        return Response({
            "profile": DoctorSerializer(doctor).data,
            "appointments": AppointmentSerializer(appointments, many=True).data,
            "patients": PatientSerializer(patients, many=True).data,
        })


# === View-only: Doctor Basic Info

class DoctorInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

    def get(self, request):
        doctor = get_object_or_404(Doctor, user=request.user)
        return Response(DoctorSerializer(doctor).data)


# === CRUD for Doctor Schedule

class CreateDoctorScheduleView(generics.CreateAPIView):
    serializer_class = DoctorScheduleSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

    def perform_create(self, serializer):
        doctor = get_object_or_404(Doctor, user=self.request.user)
        serializer.save(doctor=doctor)


class UpdateDoctorScheduleView(generics.UpdateAPIView):
    queryset = DoctorSchedule.objects.all()
    serializer_class = DoctorScheduleSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]


class DeleteDoctorScheduleView(generics.DestroyAPIView):
    queryset = DoctorSchedule.objects.all()
    serializer_class = DoctorScheduleSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

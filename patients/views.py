# patients/permissions.py
from rest_framework.permissions import IsAuthenticated
from doctors.serializers import DoctorSerializer
from appointments.serializers import AppointmentSerializer
from appointments.models import Appointment
from .serializers import *
from .models import *
from doctors.models import Doctor
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import permissions
from rest_framework.exceptions import NotFound


class IsPatientUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_patient', False)


# ========== PUBLICALLY ACCESSIBLE CREATION VIEWS FOR BASE MODELS ==========
class CreateAllergyView(generics.CreateAPIView):
    serializer_class = AllergySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]
    queryset = Allergy.objects.all()


# List views for base models
class ListAllergiesView(generics.ListAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]





# ===================== Create Patient Info ========================================

class CreatePatientView(generics.CreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateChronicDiseaseView(generics.CreateAPIView):
    serializer_class = ChronicDiseaseSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class CreateSurgeryView(generics.CreateAPIView):
    serializer_class = SurgerySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class CreateDisabilityView(generics.CreateAPIView):
    serializer_class = DisabilitySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)

class CreateEmergencyContactView(generics.CreateAPIView):
    serializer_class = EmergencyContactSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class CreatePatientAllergyView(generics.CreateAPIView):
    serializer_class = PatientAllergySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class CreateAppointmentView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)
        

class CreateVisitView(generics.CreateAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)
        
        
        
        
        
# === List Patient Profile Info ===

class PatientProfileView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        profile_data = PatientSerializer(patient).data
        return Response(profile_data)


class PatientEmergencyContactView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        emergency_contact = getattr(patient, 'emergency_contact', None)
        if emergency_contact:
            contact_data = EmergencyContactSerializer(emergency_contact).data
            return Response(contact_data)
        return Response({"detail": "No emergency contact found."}, status=404)


class ChronicDiseasesView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        return Response(ChronicDiseaseSerializer(patient.chronic_diseases.all(), many=True).data)


class SurgeriesView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        return Response(SurgerySerializer(patient.surgeries.all(), many=True).data)
    

class DisabilitiesView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        return Response(DisabilitySerializer(patient.disabilities.all(), many=True).data)


class PatientAppointmentsView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        appointments = Appointment.objects.filter(
            patient=patient).order_by('date', 'time')
        return Response(AppointmentSerializer(appointments, many=True).data)


class PatientDoctorsView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        doctors = Doctor.objects.filter(
            appointments__patient=patient).distinct()
        return Response(DoctorSerializer(doctors, many=True).data)


class PatientAllergiesView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        return Response(PatientAllergySerializer(patient.allergies.all(), many=True).data)



class PatientVisitsView(generics.ListAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Visit.objects.filter(patient=patient).order_by('-visit_date')


# ----------- UPDATE + DELETE VIEWS -----------

class UpdatePatientView(generics.RetrieveUpdateAPIView):
    serializer_class = PatientSerializer
    # Assuming IsPatientUser is custom
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_object(self):
        try:
            return Patient.objects.get(user=self.request.user)
        except Patient.DoesNotExist:
            raise NotFound("Patient profile not found.")



# === Emergency Contact ===
class UpdateEmergencyContactView(generics.UpdateAPIView):
    serializer_class = EmergencyContactSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return EmergencyContact.objects.filter(patient=patient)


class DeleteEmergencyContactView(generics.DestroyAPIView):
    serializer_class = EmergencyContactSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return EmergencyContact.objects.filter(patient=patient)


# === Allergy ===
class UpdatePatientAllergyView(generics.UpdateAPIView):
    serializer_class = PatientAllergySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return PatientAllergy.objects.filter(patient=patient)


class DeletePatientAllergyView(generics.DestroyAPIView):
    serializer_class = PatientAllergySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return PatientAllergy.objects.filter(patient=patient)


# === Chronic Disease ===
class UpdateChronicDiseaseView(generics.UpdateAPIView):
    serializer_class = ChronicDiseaseSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return ChronicDisease.objects.filter(patient=patient)


class DeleteChronicDiseaseView(generics.DestroyAPIView):
    serializer_class = ChronicDiseaseSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return ChronicDisease.objects.filter(patient=patient)


# === Surgery ===
class UpdateSurgeryView(generics.UpdateAPIView):
    serializer_class = SurgerySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Surgery.objects.filter(patient=patient)


class DeleteSurgeryView(generics.DestroyAPIView):
    serializer_class = SurgerySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Surgery.objects.filter(patient=patient)


# === Disability ===
class UpdateDisabilityView(generics.UpdateAPIView):
    serializer_class = DisabilitySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Disability.objects.filter(patient=patient)


class DeleteDisabilityView(generics.DestroyAPIView):
    serializer_class = DisabilitySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Disability.objects.filter(patient=patient)


# === Appointment ===
class UpdateAppointmentView(generics.UpdateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Appointment.objects.filter(patient=patient)


class DeleteAppointmentView(generics.DestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Appointment.objects.filter(patient=patient)


# === Visit ===
class UpdateVisitView(generics.UpdateAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Visit.objects.filter(patient=patient)


class DeleteVisitView(generics.DestroyAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Visit.objects.filter(patient=patient)

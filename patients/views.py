# patients/permissions.py
from rest_framework.permissions import AllowAny, IsAuthenticated
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


class IsPatientUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_patient', False)


# ========== PUBLICALLY ACCESSIBLE CREATION VIEWS FOR BASE MODELS ==========


class CreateAllergyView(generics.CreateAPIView):
    serializer_class = AllergySerializer
    permission_classes = [AllowAny]
    queryset = Allergy.objects.all()


class CreateChronicDiseaseView(generics.CreateAPIView):
    serializer_class = ChronicDiseaseSerializer
    permission_classes = [AllowAny]
    queryset = ChronicDisease.objects.all()


class CreateSurgeryView(generics.CreateAPIView):
    serializer_class = SurgerySerializer
    permission_classes = [AllowAny]
    queryset = Surgery.objects.all()


class CreateDisabilityView(generics.CreateAPIView):
    serializer_class = DisabilitySerializer
    permission_classes = [AllowAny]
    queryset = Disability.objects.all()


# List views for base models
class ListAllergiesView(generics.ListAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    permission_classes = [AllowAny]


class ListChronicDiseasesView(generics.ListAPIView):
    queryset = ChronicDisease.objects.all()
    serializer_class = ChronicDiseaseSerializer
    permission_classes = [AllowAny]


class ListSurgeriesView(generics.ListAPIView):
    queryset = Surgery.objects.all()
    serializer_class = SurgerySerializer
    permission_classes = [AllowAny]


class ListDisabilitiesView(generics.ListAPIView):
    queryset = Disability.objects.all()
    serializer_class = DisabilitySerializer
    permission_classes = [AllowAny]





# =============================================================

class CreatePatientView(generics.CreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




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


class CreatePatientChronicDiseaseView(generics.CreateAPIView):
    serializer_class = PatientChronicDiseaseSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class CreatePatientSurgeryView(generics.CreateAPIView):
    serializer_class = PatientSurgerySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class CreatePatientDisabilityView(generics.CreateAPIView):
    serializer_class = PatientDisabilitySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class CreatePatientMedicationView(generics.CreateAPIView):
    serializer_class = PatientMedicationSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)
        
        
# === Patient Profile Info ===

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


class PatientMedicationsView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        medications = PatientMedication.objects.filter(patient=patient)
        return Response(PatientMedicationSerializer(medications, many=True).data)


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


class PatientChronicDiseasesView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        return Response(PatientChronicDiseaseSerializer(patient.chronic_diseases.all(), many=True).data)


class PatientSurgeriesView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        return Response(PatientSurgerySerializer(patient.surgeries.all(), many=True).data)


class PatientDisabilitiesView(APIView):
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get(self, request):
        patient = get_object_or_404(Patient, user=request.user)
        return Response(PatientDisabilitySerializer(patient.disabilities.all(), many=True).data)


class CreateVisitView(generics.CreateAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, user=self.request.user)
        serializer.save(patient=patient)


class ListMyVisitsView(generics.ListAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_queryset(self):
        patient = get_object_or_404(Patient, user=self.request.user)
        return Visit.objects.filter(patient=patient).order_by('-visit_date')


# ----------- UPDATE + DELETE VIEWS -----------

class UpdatePatientView(generics.UpdateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

    def get_object(self):
        return get_object_or_404(Patient, user=self.request.user)


class UpdateEmergencyContactView(generics.UpdateAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class DeleteEmergencyContactView(generics.DestroyAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class UpdatePatientAllergyView(generics.UpdateAPIView):
    queryset = PatientAllergy.objects.all()
    serializer_class = PatientAllergySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class DeletePatientAllergyView(generics.DestroyAPIView):
    queryset = PatientAllergy.objects.all()
    serializer_class = PatientAllergySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class UpdatePatientChronicDiseaseView(generics.UpdateAPIView):
    queryset = PatientChronicDisease.objects.all()
    serializer_class = PatientChronicDiseaseSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class DeletePatientChronicDiseaseView(generics.DestroyAPIView):
    queryset = PatientChronicDisease.objects.all()
    serializer_class = PatientChronicDiseaseSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class UpdatePatientSurgeryView(generics.UpdateAPIView):
    queryset = PatientSurgery.objects.all()
    serializer_class = PatientSurgerySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class DeletePatientSurgeryView(generics.DestroyAPIView):
    queryset = PatientSurgery.objects.all()
    serializer_class = PatientSurgerySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class UpdatePatientDisabilityView(generics.UpdateAPIView):
    queryset = PatientDisability.objects.all()
    serializer_class = PatientDisabilitySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class DeletePatientDisabilityView(generics.DestroyAPIView):
    queryset = PatientDisability.objects.all()
    serializer_class = PatientDisabilitySerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class UpdatePatientMedicationView(generics.UpdateAPIView):
    queryset = PatientMedication.objects.all()
    serializer_class = PatientMedicationSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]


class DeletePatientMedicationView(generics.DestroyAPIView):
    queryset = PatientMedication.objects.all()
    serializer_class = PatientMedicationSerializer
    permission_classes = [IsAuthenticated, IsPatientUser]

from django.shortcuts import render

from rest_framework import viewsets
from .models import *
from .serializers import *


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class PatientAllergyViewSet(viewsets.ModelViewSet):
    queryset = PatientAllergy.objects.all()
    serializer_class = PatientAllergySerializer


class PatientChronicDiseaseViewSet(viewsets.ModelViewSet):
    queryset = PatientChronicDisease.objects.all()
    serializer_class = PatientChronicDiseaseSerializer


class PatientSurgeryViewSet(viewsets.ModelViewSet):
    queryset = PatientSurgery.objects.all()
    serializer_class = PatientSurgerySerializer


class PatientDisabilityViewSet(viewsets.ModelViewSet):
    queryset = PatientDisability.objects.all()
    serializer_class = PatientDisabilitySerializer


class PatientMedicationViewSet(viewsets.ModelViewSet):
    queryset = PatientMedication.objects.all()
    serializer_class = PatientMedicationSerializer

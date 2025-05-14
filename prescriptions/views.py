from rest_framework import viewsets
from .models import Prescription, PrescriptionMedication, Medication
from .serializers import PrescriptionSerializer, PrescriptionMedicationSerializer, MedicationSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionMedicationViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

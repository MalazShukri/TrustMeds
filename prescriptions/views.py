from rest_framework import generics, permissions
from .models import Prescription, PrescriptionMedication, Medication
from .serializers import PrescriptionSerializer, PrescriptionMedicationSerializer, MedicationSerializer

# Medications API's
class MedicationCreateView(generics.CreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationListView(generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationDetailView(generics.RetrieveAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationUpdateView(generics.UpdateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationDeleteView(generics.DestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer




# Prescriptions API's
class PrescriptionCreateView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionListView(generics.ListAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionDetailView(generics.RetrieveAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionUpdateView(generics.UpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionDeleteView(generics.DestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer




# Prescriptions Medications API's
class PrescriptionMedicationCreateView(generics.CreateAPIView):
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer


class PrescriptionMedicationListView(generics.ListAPIView):
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer


class PrescriptionMedicationDetailView(generics.RetrieveAPIView):
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer


class PrescriptionMedicationUpdateView(generics.UpdateAPIView):
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer


class PrescriptionMedicationDeleteView(generics.DestroyAPIView):
    queryset = PrescriptionMedication.objects.all()
    serializer_class = PrescriptionMedicationSerializer

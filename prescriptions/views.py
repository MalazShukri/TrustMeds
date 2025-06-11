from rest_framework import generics, permissions
from .models import Prescription, Medication
from .serializers import PrescriptionSerializer, MedicationSerializer
from rest_framework.exceptions import ValidationError



class IsDoctorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_doctor', False)
    
    
# === PRESCRIPTION VIEWS ===

class PrescriptionCreateView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

    def perform_create(self, serializer):
        doctor = self.request.user.doctor
        patient_id = self.request.data.get("patient")

        if not patient_id:
            raise ValidationError(
                {"patient": "This field is required."})

        try:
            from patients.models import Patient
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise ValidationError({"patient": "Invalid patient ID."})

        serializer.save(doctor=doctor, patient=patient)



class MyPrescriptionsView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'patient'):
            return Prescription.objects.filter(patient=user.patient)
        return Prescription.objects.none()



class DoctorPrescriptionsView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]

    def get_queryset(self):
        return Prescription.objects.filter(doctor=self.request.user.doctor)



class MyPrescriptionDetailView(generics.RetrieveAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'patient'):
            return Prescription.objects.filter(patient=user.patient)
        return Prescription.objects.none()




class PrescriptionUpdateView(generics.UpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]


class PrescriptionDeleteView(generics.DestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]





# === MEDICATION VIEWS ===

class MedicationCreateView(generics.CreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]


class MedicationListView(generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicationDetailView(generics.RetrieveAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicationUpdateView(generics.UpdateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorUser]


class MedicationDeleteView(generics.DestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]

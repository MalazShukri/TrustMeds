from django.urls import path
from .views import *

urlpatterns = [
    # Prescription
    path('my-prescriptions/', MyPrescriptionsView.as_view(),
         name='my-prescriptions'),
    path('doctor-prescriptions/', DoctorPrescriptionsView.as_view(),
         name='doctor-prescriptions'),
    path('prescriptions/create/', PrescriptionCreateView.as_view(),
         name='prescription-create'),
    path('my-prescriptions/<int:pk>/', MyPrescriptionDetailView.as_view(),
         name='my-prescription-detail'),
    path('prescriptions/<int:pk>/update/',
         PrescriptionUpdateView.as_view(), name='prescription-update'),
    path('prescriptions/<int:pk>/delete/',
         PrescriptionDeleteView.as_view(), name='prescription-delete'),

    # Medication
    path('medications/', MedicationListView.as_view(), name='medication-list'),
    path('medications/create/', MedicationCreateView.as_view(),
         name='medication-create'),
    path('medications/<int:pk>/', MedicationDetailView.as_view(),
         name='medication-detail'),
    path('medications/<int:pk>/update/',
         MedicationUpdateView.as_view(), name='medication-update'),
    path('medications/<int:pk>/delete/',
         MedicationDeleteView.as_view(), name='medication-delete'),
]

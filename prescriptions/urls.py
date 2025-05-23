from django.urls import path
from .views import *

urlpatterns = [
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

    # Prescription
    path('prescriptions/', PrescriptionListView.as_view(),
         name='prescription-list'),
    path('prescriptions/create/', PrescriptionCreateView.as_view(),
         name='prescription-create'),
    path('prescriptions/<int:pk>/', PrescriptionDetailView.as_view(),
         name='prescription-detail'),
    path('prescriptions/<int:pk>/update/',
         PrescriptionUpdateView.as_view(), name='prescription-update'),
    path('prescriptions/<int:pk>/delete/',
         PrescriptionDeleteView.as_view(), name='prescription-delete'),

    # PrescriptionMedication
    path('prescription-medications/', PrescriptionMedicationListView.as_view(),
         name='prescriptionmedication-list'),
    path('prescription-medications/create/',
         PrescriptionMedicationCreateView.as_view(), name='prescriptionmedication-create'),
    path('prescription-medications/<int:pk>/',
         PrescriptionMedicationDetailView.as_view(), name='prescriptionmedication-detail'),
    path('prescription-medications/<int:pk>/update/',
         PrescriptionMedicationUpdateView.as_view(), name='prescriptionmedication-update'),
    path('prescription-medications/<int:pk>/delete/',
         PrescriptionMedicationDeleteView.as_view(), name='prescriptionmedication-delete'),
]

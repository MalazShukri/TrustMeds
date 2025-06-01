from django.urls import path
from .views import *

urlpatterns = [
    # === Publicly accessible creation endpoints for base models ==
    path('public/create-allergy/', CreateAllergyView.as_view(),
         name='create-allergy-base'),
    path('public/create-chronic-disease/',
         CreateChronicDiseaseView.as_view(), name='create-chronic-disease-base'),
    path('public/create-surgery/', CreateSurgeryView.as_view(),
         name='create-surgery-base'),
    path('public/create-disability/', CreateDisabilityView.as_view(),
         name='create-disability-base'),
    
    # === Public GET list endpoints for base models ===
    path('public/allergies/', ListAllergiesView.as_view(), name='list-allergies'),
    path('public/chronic-diseases/', ListChronicDiseasesView.as_view(),
         name='list-chronic-diseases'),
    path('public/surgeries/', ListSurgeriesView.as_view(), name='list-surgeries'),
    path('public/disabilities/', ListDisabilitiesView.as_view(),
         name='list-disabilities'),



    # === Patient Profile APIs ===
    path('create-patient/',
         CreatePatientView.as_view(), name='create-patient'),
    path('me/profile/', PatientProfileView.as_view(), name='patient-profile'),
    path('me/emergency-contact/', PatientEmergencyContactView.as_view(),
         name='patient-emergency-contact'),
    path('me/update-profile/', UpdatePatientView.as_view(),
         name='update-patient-profile'),


    # === Patient Home Sections ===
    path('me/medications/', PatientMedicationsView.as_view(),
         name='patient-medications'),
    path('me/appointments/', PatientAppointmentsView.as_view(),
         name='patient-appointments'),
    path('me/doctors/', PatientDoctorsView.as_view(), name='patient-doctors'),
    path('create-visit/', CreateVisitView.as_view(), name='create-visit'),
    path('me/visits/', ListMyVisitsView.as_view(), name='my-visits'),

    # === Patient Health Summary Sections ===
    path('me/allergies/', PatientAllergiesView.as_view(), name='patient-allergies'),
    path('me/chronic-diseases/', PatientChronicDiseasesView.as_view(),
         name='patient-chronic-diseases'),
    path('me/surgeries/', PatientSurgeriesView.as_view(), name='patient-surgeries'),
    path('me/disabilities/', PatientDisabilitiesView.as_view(),
         name='patient-disabilities'),


    # === Emergency Contact ===
    path('create-emergency-contact/', CreateEmergencyContactView.as_view(),
         name='create-emergency-contact'),
    path('update-emergency-contact/<int:pk>/',
         UpdateEmergencyContactView.as_view(), name='update-emergency-contact'),
    path('delete-emergency-contact/<int:pk>/',
         DeleteEmergencyContactView.as_view(), name='delete-emergency-contact'),

    # === Allergy ===
    path('create-allergy/', CreatePatientAllergyView.as_view(),
         name='create-allergy'),
    path('update-allergy/<int:pk>/',
         UpdatePatientAllergyView.as_view(), name='update-allergy'),
    path('delete-allergy/<int:pk>/',
         DeletePatientAllergyView.as_view(), name='delete-allergy'),

    # === Chronic Disease ===
    path('create-chronic-disease/', CreatePatientChronicDiseaseView.as_view(),
         name='create-chronic-disease'),
    path('update-chronic-disease/<int:pk>/',
         UpdatePatientChronicDiseaseView.as_view(), name='update-chronic-disease'),
    path('delete-chronic-disease/<int:pk>/',
         DeletePatientChronicDiseaseView.as_view(), name='delete-chronic-disease'),

    # === Surgery ===
    path('create-surgery/', CreatePatientSurgeryView.as_view(),
         name='create-surgery'),
    path('update-surgery/<int:pk>/',
         UpdatePatientSurgeryView.as_view(), name='update-surgery'),
    path('delete-surgery/<int:pk>/',
         DeletePatientSurgeryView.as_view(), name='delete-surgery'),

    # === Disability ===
    path('create-disability/', CreatePatientDisabilityView.as_view(),
         name='create-disability'),
    path('update-disability/<int:pk>/',
         UpdatePatientDisabilityView.as_view(), name='update-disability'),
    path('delete-disability/<int:pk>/',
         DeletePatientDisabilityView.as_view(), name='delete-disability'),

    # === Medication ===
    path('create-medication/', CreatePatientMedicationView.as_view(),
         name='create-medication'),
    path('update-medication/<int:pk>/',
         UpdatePatientMedicationView.as_view(), name='update-medication'),
    path('delete-medication/<int:pk>/',
         DeletePatientMedicationView.as_view(), name='delete-medication'),
    
    
    # === Appointment Management ===
    path('create-appointment/', CreateAppointmentView.as_view(),
         name='create-appointment'),
#     path('update-appointment/<int:pk>/',
#          UpdateAppointmentView.as_view(), name='update-appointment'),
#     path('delete-appointment/<int:pk>/',
#          DeleteAppointmentView.as_view(), name='delete-appointment'),

    # === Visit Management ===
#     path('update-visit/<int:pk>/', UpdateVisitView.as_view(), name='update-visit'),
#     path('delete-visit/<int:pk>/', DeleteVisitView.as_view(), name='delete-visit'),

]

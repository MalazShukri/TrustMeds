from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('', PatientViewSet, basename='patient')
router.register('emergency-contacts', EmergencyContactViewSet)
router.register('visits', VisitViewSet)
router.register('allergies', PatientAllergyViewSet)
router.register('chronic-diseases', PatientChronicDiseaseViewSet)
router.register('surgeries', PatientSurgeryViewSet)
router.register('disabilities', PatientDisabilityViewSet)
router.register('medications', PatientMedicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

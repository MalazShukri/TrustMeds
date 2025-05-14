from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PrescriptionViewSet, PrescriptionMedicationViewSet, MedicationViewSet

router = DefaultRouter()
router.register('', PrescriptionViewSet, basename='prescription')
router.register('medications', PrescriptionMedicationViewSet,
                basename='prescription-medication')
router.register('available-meds', MedicationViewSet, basename='medication')

urlpatterns = [
    path('', include(router.urls)),
]

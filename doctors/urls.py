from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DoctorViewSet, DoctorScheduleViewSet

router = DefaultRouter()
router.register('', DoctorViewSet, basename='doctor')
router.register('schedules', DoctorScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', include(router.urls)),
]

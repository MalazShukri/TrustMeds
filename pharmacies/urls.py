from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PharmacyViewSet

router = DefaultRouter()
router.register('', PharmacyViewSet, basename='pharmacy')

urlpatterns = [
    path('', include(router.urls)),
]

from django.shortcuts import render
from rest_framework import viewsets
from .models import Pharmacy
from .serializers import PharmacySerializer


class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

from django.contrib import admin
from .models import Pharmacy


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'phone_number',
                    'email', 'is_active', 'created_at')
    search_fields = ('name', 'license_number')
    list_filter = ('is_active',)

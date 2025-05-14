from django.contrib import admin
from .models import Doctor, DoctorSchedule


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'email',
                    'phone_number', 'is_active', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'specialization')
    list_filter = ('specialization', 'is_active')


@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('day_of_week',)

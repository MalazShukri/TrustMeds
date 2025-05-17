from django.urls import path
from .views import (
    DoctorFullProfileView, DoctorInfoView,
    CreateDoctorScheduleView, UpdateDoctorScheduleView, DeleteDoctorScheduleView,
    CreateDoctorProfileView, UpdateDoctorProfileView,
)

urlpatterns = [
     
    path('create-profile/', CreateDoctorProfileView.as_view(),
         name='create-doctor-profile'),
    path('update-profile/', UpdateDoctorProfileView.as_view(),
         name='update-doctor-profile'),
    
    # === Full doctor profile (/me)
    path('me/', DoctorFullProfileView.as_view(), name='doctor-me'),

    # === Basic doctor info (view only)
    path('info/', DoctorInfoView.as_view(), name='doctor-info'),

    # === Doctor Schedule
    path('create-schedule/', CreateDoctorScheduleView.as_view(),
         name='create-schedule'),
    path('update-schedule/<int:pk>/',
         UpdateDoctorScheduleView.as_view(), name='update-schedule'),
    path('delete-schedule/<int:pk>/',
         DeleteDoctorScheduleView.as_view(), name='delete-schedule'),
]

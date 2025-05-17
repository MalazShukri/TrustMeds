from django.urls import path
from .views import *

urlpatterns = [
    path('patients/signup/', PatientSignupView.as_view(), name='patient_signup'),
    path('patients/login/', PatientLoginView.as_view(), name='patient_login'),
    path('doctors/signup/', DoctorSignupView.as_view(), name='doctor_signup'),
    path('doctors/login/', DoctorLoginView.as_view(), name='doctor_login'),
    path('pharmacies/signup/', PharmacySignupView.as_view(),
         name='pharmacist_signup'),
    path('pharmacies/login/', PharmacyLoginView.as_view(), name='pharmacist_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

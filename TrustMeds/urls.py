from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patients/', include('patients.urls')),
    # path('api/doctors/', include('doctors.urls')),
    # path('api/pharmacies/', include('pharmacies.urls')),
    # path('api/prescriptions/', include('prescriptions.urls')),
    # path('api/accounts/', include('accounts.urls')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/patients/', include('patients.urls')),
    # path('api/doctors/', include('doctors.urls')),
    # path('api/pharmacists/', include('pharmacists.urls')),
    # path('api/accounts/', include('accounts.urls')),
]

from django.urls import path
from .views import AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView

urlpatterns = [
    path('', AppointmentListCreateView.as_view(),
         name='appointment-list-create'),
    path('<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view(),
         name='appointment-detail'),
]

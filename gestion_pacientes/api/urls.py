from django.urls import path
from gestion_pacientes.api.api import PacienteAPIView

urlpatterns = [path("paciente/", PacienteAPIView.as_view())]

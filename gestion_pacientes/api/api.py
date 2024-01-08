from rest_framework.response import Response
from rest_framework.views import APIView
from gestion_pacientes.models import Paciente
from rest_framework import status
from .serializers import PacienteSerializer


class PacienteAPIView(APIView):
    def get(self, request):
        pacientes = Paciente.objects.all()
        paciente_serializer = PacienteSerializer(pacientes, many=True)
        return Response(paciente_serializer.data)

    def post(self, request, *args, **kwargs):
        paciente_serializer = PacienteSerializer(data=request.data)
        if paciente_serializer.is_valid():
            paciente_serializer.save()
            return Response(paciente_serializer.data, status=status.HTTP_201_CREATED)
        return Response(paciente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

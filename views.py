from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MascotasSerializable
from .serializers import MedicamentossSerializable

from .models import Mascotas
from .models import Medicamentos

# Create your views here.
class MascotasVista(viewsets.ModelViewSet):
    serializer_class:MascotasSerializable
    queryset=Mascotas.objects.all()
class MedicamentosVista(viewsets.ModelViewSet):
    serializer_class: MedicamentosSerializable
    queryset=Medicamentos.objects.all()

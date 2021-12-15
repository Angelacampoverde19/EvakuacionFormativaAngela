from rest_framework import serializers 
from .models import Mascotas
from .models import Medicamentos

class MascotasSerializable(serializers.ModelSerializer):
    class Meta:
        model=Mascotas
        fields=(
            'tipo',
            'raza',
            'tamaño'
        )

class MedicamentosSerializable(serializers.ModelSerializer):
    class Meta:
        model= Medicamentos
        fields=(
            'marca',
            'precio',
            'tipo'
        )

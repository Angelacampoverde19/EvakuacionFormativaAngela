from django.db import models

# Create your models here.
class Mascotas(models.Model):
    raza=models.CharField(max_length=120, help_text='Ingrese la raza.')
    tipo=models.CharField(max_length=120, help_text='Ingrese el tipo de mascota.')
    tamaño=models.CharField(max_length=1000,help_text='Ingrese el tamaño de la mascota')

class Medicamentos(models.Model):
    marca=models.CharField(max_length=200,help_text='Ingrese marca del medicamento')
    precio=models.CharField(help_text='Ingrese el precio de medicamento')
    tipo=models.CharField(help_text='Ingrese el tipo de medicamento')




    
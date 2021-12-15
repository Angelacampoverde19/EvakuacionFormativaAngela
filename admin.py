from django.contrib import admin
from .models import Mascotas
from .models import Medicamentos

# Register your models here.
admin.site.register(Mascotas)
admin.site.register(Medicamentos)


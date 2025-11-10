from django.contrib import admin
from .models import Empleado, Cliente, Venta

# Registra tus modelos aquí.
admin.site.register(Empleado)
admin.site.register(Cliente) # <--- Descomentar esta línea
# admin.site.register(Venta)   # Dejar comentada por ahora
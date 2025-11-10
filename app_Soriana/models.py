from django.db import models

# ==========================================
# MODELO: Empleado
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Cliente
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Venta
# ==========================================
class Venta(models.Model):
    # Relación de Uno a Muchos: Un empleado puede realizar muchas ventas
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='ventas_realizadas')
    
    # Relación de Muchos a Muchos: Una venta puede incluir a varios clientes (e.g., padres pagando por un hijo),
    # y un cliente puede estar en varias ventas (e.g., pagos a plazos o inscripciones múltiples)
    clientes = models.ManyToManyField(Cliente, related_name='compras')

    fecha_venta = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    estado_venta = models.CharField(max_length=50, default='Completada')

    def __str__(self):
        return f"Venta {self.id} - {self.fecha_venta}"
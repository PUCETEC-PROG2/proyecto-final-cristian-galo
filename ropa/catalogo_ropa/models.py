from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    apellidos = models.CharField(max_length=150, null=False)
    cedula = models.BigIntegerField(null=False)
    telefono = models.BigIntegerField(null=False)
    correo = models.EmailField(null=False)

    def __str__(self) -> str:
        return f'{self.apellidos} {self.nombre}'

from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100, verbose_name='Nombre de la Categoría')

    def __str__(self):
        return self.nombre_categoria



class Producto(models.Model):
    
    nombre_producto = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    talla = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre_producto





class Compra(models.Model):
    ciudad = models.CharField(max_length=50, null=False)
    fecha_compra = models.DateField(null=False)
    precio_total = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    productos = models.ManyToManyField(Producto)

    def __str__(self) -> str:
        return f'Compra de {self.cliente} - {self.fecha_compra}'

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.cantidad} x {self.producto.nombre_producto}' 
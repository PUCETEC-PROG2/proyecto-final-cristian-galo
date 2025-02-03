from django.contrib import admin
from .models import Cliente, Categoria, Producto, Compra, DetalleCompra

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    pass

@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "categoria")
    search_fields = ("nombre",)
    list_filter = ("categoria",)
    ordering = ("nombre",)
# Register your models here.

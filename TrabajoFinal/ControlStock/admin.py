from django.contrib import admin
from .models import Producto, Proveedor

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio','StockActual']
    search_fields =['nombre', 'StockActual']

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['apellido','dni']
    search_fields =['apellido', 'dni']






admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)



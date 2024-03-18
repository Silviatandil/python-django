from django.contrib import admin
from .models import producto

# Register your models here.

class productoAdmin(admin.ModelAdmin):
    list_display =  ['titulo','categoria', 'precio']
    search_fields = ['color']

admin.site.register(producto, productoAdmin)

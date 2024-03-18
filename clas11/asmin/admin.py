from django.contrib import admin
from .models import Libro

class libroAdmin(admin.ModelAdmin):
    list_display = ['titulo','autor', 'año']
    search_fields = ['titulo','autor', 'año']



admin.site.register(Libro, libroAdmin)



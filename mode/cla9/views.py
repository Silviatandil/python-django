from django.shortcuts import render
from .models import Auto

def Crear_Auto(request):
    auto = Auto.objects.create(
        Marca = "Ford",
        Modelo = "2024",
        Color = "Rojo"
    )
    return render(request, 'auto.html', {'Auto' : auto})


# Create your views here.

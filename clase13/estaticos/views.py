from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

def mostrar_index(request):
    ruta = "C:/Users/camar/Desktop/DJANGO2/clase13/estaticos/templates/index.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    return HttpResponse(plantilla.render(contexto))




def mostrar_otro(request):
    ruta = "C:/Users/camar/Desktop/DJANGO2/clase13/estaticos/templates/otro.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    return HttpResponse(plantilla.render(contexto))
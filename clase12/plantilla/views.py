from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse


def saludo2(request):
    estudiantes_inscriptos = [
        {"nombre": "Juan", "cursos_realizados": [
            {"titulo": "django", "desc": "framework de python"},
            {"titulo": "css", "desc": "bases del diseño web"},
            {"titulo": "javascript", "desc": "Dinamismo de la pagina"}
        ]},
        {"nombre": "Carla","cursos_realizados": [
            {"titulo": "react", "desc": "framework de javascript"}
        ]},
            {"nombre": "Tito","cursos_realizados": []}
    ]
        
#def saludo(request):
    #nombre_estudiante = "Carlos"
    doc_externo = open("C:/Users/camar/Desktop/DJANGO2/clase12/plantilla/templates/index.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes":estudiantes_inscriptos})
    return HttpResponse(plantilla.render(contexto))


       




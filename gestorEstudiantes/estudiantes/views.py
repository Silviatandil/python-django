from django.shortcuts import render
from .models import estudiantes

def crear_estudiantes(request,nombre, apellido, edad, nota):
    estudiante = estudiantes.objects.create(
    nombre = nombre,
    apellido = apellido,
    edad = edad,
    nota = nota
    )
    return render(request,'estudiantes.html', {'estudiante':estudiante})

def mostrar_estudiante(request):
    lista_estudiantes = estudiantes.objects.all()
    return render(request,'lista_estudiantes.html',{'lista_estudiantes': lista_estudiantes})

def filtrar_estudiante_nota(request,nota):
    estudianteEncontrado = estudiantes.objects.filter(nota = nota)
    return render(request,'estudiante_filtrado.html', {'estudianteEncontrado': estudianteEncontrado})

def update_estudiante_id(request, id, nombre, apellido, edad, nota):
    estudianteActualizar = estudiantes.objects.get(id = id)
    estudianteActualizar.nombre = nombre
    estudianteActualizar.apellido = apellido
    estudianteActualizar.edad = edad
    estudianteActualizar.nota = nota
    estudianteActualizar.save()
    estudiante = estudiantes.objects.all()
    return render (request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def borrar_estudiante_id(request, id):
    estudianteBorrar= estudiantes.objects.get(id = id)
    estudianteBorrar.delete()
    estudiante = estudiantes.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes':estudiante})

def borrar_estudiante(request):
    estudiante = estudiantes.objects.all()
    estudiante.delete()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiante})



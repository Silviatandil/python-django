from django.shortcuts import render
from .models import Usuario
#instancia del modelo
def crear_usuario(request, nombre, apellido, edad):
    nuevo_usuario = Usuario.objects.create(
        nombre = nombre,
        apellido = apellido,
        edad = edad
    )
    return render(request, 'nuevo_usuario.html', {'nuevo_usuario': nuevo_usuario})

#crear la funcion read.listar todos los usuarios
def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,'lista_usuarios.html', {'usuarios': usuarios})

def filtrar_usuarios_edad(request):
   usuariosEncontrados = Usuario.objects.filter(edad = 28)
   return render(request, 'usuarios_filtrados.html', {'usuariosEcontrados': usuariosEncontrados})

#actualizar usuario por id
def update_usuarios_id(request,id, nombre, apellido, edad):
    usuarioActualizar = Usuario.objects.get(id = id)
    usuarioActualizar.nombre = nombre
    usuarioActualizar.apellido = apellido
    usuarioActualizar.edad = edad
    usuarioActualizar.save()
    usuarios = Usuario.objects.all()
    return render(request,'lista_usuarios.html', {'usuarios': usuarios})
 #borrar por id
def borrar_usuario_id(request, id):
    usuarioBorrar = Usuario.objects.get(id = id)
    usuarioBorrar.delete()
    usuarios = Usuario.objects.all()
    return render(request,'lista_usuarios.html', {'usuarios': usuarios})
     
#borrar todo
def borrar_usuarios(request):
    usuarios = Usuario.objects.all()
    usuarios.delete()
    return render(request,'lista_usuarios.html', {'usuarios': usuarios})
     


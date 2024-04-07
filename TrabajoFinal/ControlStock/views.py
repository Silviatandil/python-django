from django.shortcuts import render
from .models import Producto, Proveedor

def crearProducto(request,nombre, precio, StockActual):
    producto = Producto.objects.create(
        nombre = nombre,
        precio = precio,
        StockActual = StockActual
    )
    return render(request,'crear_producto.html', {'producto': producto})

def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})

def filtrar_productos_stock(request):
    productoEncontrado = Producto.objects.filter(StockActual=2)
    print(productoEncontrado)
    return render(request, 'productoEncontrado.html', {'productoEncontrado': productoEncontrado})

def update_producto_id(request, id, nombre, precio, StockActual):
    productoActualizar = Producto.objects.get(id = id)
    productoActualizar.nombre = nombre
    productoActualizar.precio = precio
    productoActualizar.StockActual = StockActual
    productoActualizar.save()
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})

def borrarProducto_id(request, id):
    productoBorrar = Producto.objects.get(id = id)
    productoBorrar.delete()
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})

def borrarProducto(request):
    productos = Producto.objects.all()
    productos.delete()
    return render(request, 'lista_producto.html', {'productos': productos})


def crearProveedor(request, nombre, apellido, dni):
    proveedor = Proveedor.objects.create(
        nombre = nombre,
        apellido = apellido,
        dni = dni
    )   
    return render(request,'crear_proveedor.html', {'proveedor': proveedor})

def mostrar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores} ) 

def filtrar_proveedor_dni(request):
    proveedorEncontrado = Proveedor.objects.filter(dni = 34562239)
    return render(request, 'proveedorEncontrado.html', {'proveedorEncontrado': proveedorEncontrado}) 


def update_proveedor_dni(request, id, nombre, apellido, dni):
    proveedorActualizar = Proveedor.objects.get(id = id)
    proveedorActualizar.nombre = nombre
    proveedorActualizar.apellido = apellido
    proveedorActualizar.dni = dni
    proveedorActualizar.save()
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores} ) 

def borrarProveedor_id(request, id):
    proveedorBorrar = Proveedor.objects.get(id = id)
    proveedorBorrar.delete()
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores} ) 

def borrarProveedor(request):
    proveedores = Proveedor.objects.all()
    proveedores.delete()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores} ) 
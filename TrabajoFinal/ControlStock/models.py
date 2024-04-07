from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='producto')
    precio = models.FloatField()
    StockActual = models.IntegerField(verbose_name='Stock')
    class meta:
        ordering = ['-nombre']
    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    def __str__(self):
        return self.nombre





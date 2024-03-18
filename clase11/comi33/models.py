from django.db import models

class producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return self.titulo
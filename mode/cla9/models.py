from django.db import models

class Auto(models.Model):
    Marca = models.CharField(max_length=20)
    Modelo = models.CharField(max_length=30)
    Color = models.CharField(max_length=50)

    class meta: 
        ordering = ['Marca']

    def __str__ (self):
        return self.Marca

from django.db import models

class Libro (models.Model):
    titulo = models.CharField(
        max_length=100,
        verbose_name = 'nombre'
  )
    autor = models.CharField(max_length=100)
    año = models.CharField(max_length=100)



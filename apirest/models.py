from django.db import models

# Create your models here.
class Sensores(models.Model):
    temperatura = models.FloatField()
    peso = models.FloatField()
    humedad = models.IntegerField()

class Lecturas(models.Model):
    key = models.TextField()
    value = models.FloatField()
    data_created = models.DateTimeField(auto_now_add=True)
    #data_updated = models.DateTimeField(auto_now=True)

class Prueba(models.Model):
    nombre = models.TextField()
    edad = models.TextField()
    direccion = models.TextField()
    #data_updated = models.DateTimeField(auto_now=True)

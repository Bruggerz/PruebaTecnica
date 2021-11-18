from django.db import models

# Create your models here.

class Restaurant(models.Model):
    nombre_restaurant= models.CharField(max_length=200)
    ubicacion= models.CharField(max_length=200)
    comida=models.CharField(max_length=500)
    calificacion=models.IntegerField()
    visitado=models.BooleanField()
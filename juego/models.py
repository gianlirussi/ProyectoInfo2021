from django.db import models

# Create your models here.
from django.db import models

class Pregunta(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pregunta= models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.pregunta


class Respuesta(models.Model):
    id_pregunta= models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    opcion= models.CharField(max_length=200)
    puntaje= models.IntegerField()

    def __str__(self):
        return self.opcion

class Partida(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    resultado= models.IntegerField()


class Categoria(models.Model):
    categoria= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=800)

    def __str__(self):
        return self.categoria


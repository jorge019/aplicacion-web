from django.db import models
from django.contrib.auth.models import User


# Create your models here.
''' Cada clase es una tabal en la base de datos de la aplicacion
y los atributos de la clase (usuario, titulo, desc...) son las columnas de la tabla'''
class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, 
                                null=True,  # el valor de usuario puede ser null
                                blank=True) # si un formulario pide un registro puede estar en blanco
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True) # se pone automaticamente la fecha y hora actual

    def __str__(self):
        return self.titulo
    
    class Meta:
        '''La lista se ordena por las tareas completadas, si lo están se van al final de la lista'''
        ordering = ['completo'] 
        
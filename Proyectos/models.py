from django.db import models
from Autenticacion.models import Usuarios

# Create your models here.

class Proyectos(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - Autor: {self.id_usuario.user.username}'

class Secciones(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)

    def __str__(self):
        return f"Seccion {self.nombre} - Proyecto {self.id_proyecto}"

class Tareas(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    id_seccion = models.ForeignKey(Secciones, on_delete=models.CASCADE)
    tipo_tablero = models.IntegerField(choices=[(1, 'Por hacer'), (2, 'En proceso'), (3, 'Hecho')])  # Reemplazar con los tipos reales

    def __str__(self):
        return self.descripcion

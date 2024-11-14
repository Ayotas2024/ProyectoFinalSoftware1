from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.rol

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo User
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    # Los campos username, email, contraseña se heredan de User

    def __str__(self):
        return self.user.username

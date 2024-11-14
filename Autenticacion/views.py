# Plantillas
from django.shortcuts import render, redirect

# Modelos
from . models import *
# Mensajes
from django.contrib import messages
# Login y registro
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Permisos
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Vista home
# def home(request):
#     return render(request,'home.html')

############################# AUTENTICACIÓN #############################
# Login
def login_view(request):
    return render(request,'iniciar_sesion.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        user = authenticate(request, username=username, password=contraseña)
        if user is not None:
            login(request, user)  # Inicia la sesión del usuario
            messages.success(request,'Logeado')
            return redirect('home')  # Redirige a una página principal index.html
        else:
            messages.error(request,'Credenciales incorrectas')
            return render(request, 'iniciar_sesion.html')
    return render(request, 'iniciar_sesion.html')

# Logout
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

# Register
def register_view(request):
    return render(request,'registrarse.html')

def registrarse(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        username = request.POST['usuario']
        email = request.POST['correo']
        contraseña = request.POST['contraseña']
        id_rol = request.POST['rol']  # Obtén el ID del rol del formulario
        rol = Roles.objects.get(id_rol=id_rol)  # Obtén el objeto del rol

        # Crea el usuario de Django
        user = User.objects.create_user(username=username, email=email, password=contraseña)
        user.save()

        # Crea el usuario personalizado
        nuevo_usuario = Usuarios.objects.create(user=user, nombre=nombre, apellido=apellido, id_rol=rol)
        nuevo_usuario.save()

        # Inicia sesión automáticamente después de registrarse
        login(request, user)
        
        messages.success(request,'Registro exitoso')
        return redirect('home')

    return render(request, 'registrarse.html')

############################# CRUD Usuarios #############################
# Read
@login_required
@staff_member_required
def CRUD_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'CRUD_usuarios/usuarios.html', {'usuarios': usuarios})

# Update
@login_required
# @staff_member_required
def editar_usuario(request,user):
    usuario = Usuarios.objects.get(user=user)
    return render(request, 'CRUD_usuarios/editar_usuario.html', {'usuario': usuario})

@login_required
@staff_member_required
def editar_usuario2(request, user):
    usuario = Usuarios.objects.get(user=user)

    if request.method == 'POST':
        # Actualizamos los datos del perfil
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.user.username = request.POST['usuario']
        usuario.user.email = request.POST['correo']

        # Si el campo de contraseña es la misma no la actualiza, actualizamos la contraseña
        nueva_contraseña = request.POST.get('contraseña')
        if nueva_contraseña != usuario.user.password:
            usuario.user.set_password(nueva_contraseña)  # Encripta y actualiza la contraseña

        # Guardamos los cambios
        usuario.user.save()  # Guarda los cambios en el usuario
        usuario.save()  # Guarda los cambios en el perfil extendido

        messages.success(request, "El usuario ha sido actualizado correctamente.")
        return redirect('usuarios')  # Redirige a la vista deseada

    # Renderiza el formulario con los datos actuales
    return render(request, 'editar_usuario.html', {'usuario': usuario})

# Delete
@login_required
@staff_member_required
def eliminar_usuario(request, user):
    usuario = Usuarios.objects.get(user=user)
    usuario.delete()
    usuario2 = User.objects.get(id=user)
    usuario2.delete()

    messages.success(request, "El usuario ha sido eliminado correctamente.")
    return redirect('CRUD_usuarios')  # Redirige a la vista deseada
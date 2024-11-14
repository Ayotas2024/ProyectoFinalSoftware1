# Plantillas
from django.shortcuts import render, redirect, get_object_or_404
# Modelos
from . models import *
# Mensajes
from django.contrib import messages
# Permisos
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

####################### CRUD PROYECTOS #######################
@login_required
def CRUD_proyectos(request,user):
    # proyectos = Proyectos.objects.all()
    usuario=Usuarios.objects.get(user=user)
    proyectos=Proyectos.objects.filter(id_usuario=usuario)
    return render(request, 'CRUD_proyectos/Proyectos.html',{'proyectos':proyectos})

@login_required
def crear_proyecto_view(request):
    return render(request, 'CRUD_proyectos/crear_proyecto.html')

@login_required
def crear_proyecto(request, user):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        estado = request.POST['estado'] == "off"
        usuario=Usuarios.objects.get(user=user)

        # Crea el proyecto
        Proyectos.objects.create(
            nombre=nombre,
            estado=estado,
            id_usuario = usuario
        )
        
        messages.success(request,'Proyecto creado exitosamente')
        return redirect('CRUD_proyectos',usuario.user.id)

    return render(request, 'CRUD_proyectos/crear_proyecto.html')

@login_required
def editar_proyecto_view(request, id_proyecto):
    proyecto=Proyectos.objects.get(id_proyecto=id_proyecto)
    return render(request, 'CRUD_proyectos/Editar_proyecto.html',{'proyecto':proyecto})

@login_required
def editar_proyecto(request, id_proyecto):
    proyecto=Proyectos.objects.get(id_proyecto=id_proyecto)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        estado = request.POST.get('estado', 'off') == 'on'
        proyecto.nombre = nombre
        proyecto.estado = estado
        proyecto.save()
        messages.success(request, 'Proyecto editado con exito')
        return redirect('home')
    messages.error(request, 'Datos no validos')
    return render(request, 'CRUD_proyectos/Editar_proyecto.html',{'proyecto':proyecto})

@login_required
def eliminar_proyecto(request, id_proyecto):
    proyecto = Proyectos.objects.get(id_proyecto=id_proyecto)
    proyecto.delete()
    messages.success(request, 'Proyecto eliminado con exito')
    return redirect('home')

####################### CRUD SECCIONES #######################
@login_required
def CRUD_secciones(request,id_proyecto):
    secciones = Secciones.objects.filter(id_proyecto=id_proyecto)
    proyecto=Proyectos.objects.get(id_proyecto=id_proyecto)
    return render(request, 'CRUD_secciones/Secciones.html',{'secciones':secciones, "proyecto":proyecto})

@login_required
def crear_seccion(request, id_proyecto):
    proyecto=Proyectos.objects.get(id_proyecto=id_proyecto)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Secciones.objects.create(
            nombre=nombre,
            id_proyecto=proyecto
            )
        messages.success(request,'Seccion creada exitosamente')
        return redirect('CRUD_secciones',id_proyecto=id_proyecto)
    return render(request, 'CRUD_secciones/Crear_seccion.html',{'proyecto':proyecto})

@login_required
def editar_seccion_view(request, id_seccion):
    seccion = Secciones.objects.get(id_seccion=id_seccion)
    return render(request, 'CRUD_secciones/Editar_seccion.html',{'seccion': seccion})

@login_required
def editar_seccion(request, id_seccion):
    seccion = Secciones.objects.get(id_seccion=id_seccion)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        seccion.nombre=nombre
        seccion.save()
        messages.success(request, 'Seccion editada con exito')
        return redirect('CRUD_secciones',seccion.id_proyecto.id_proyecto)
    return render(request, 'CRUD_secciones/Editar_seccion.html',{'seccion': seccion})

@login_required
def eliminar_seccion(request, id_seccion):
    seccion = Secciones.objects.get(id_seccion=id_seccion)
    seccion.delete()
    messages.success(request, 'Seccion eliminada con exito')
    return redirect('CRUD_secciones',seccion.id_proyecto.id_proyecto)

####################### CRUD TAREAS #######################
@login_required
def CRUD_tareas(request,id_seccion):
    tareas = Tareas.objects.filter(id_seccion=id_seccion)
    seccion = Secciones.objects.get(id_seccion=id_seccion)
    return render(request, 'CRUD_tareas/Tareas.html',{'tareas':tareas,"seccion":seccion})

@login_required
def crear_tarea_view(request,id_seccion):
    seccion = Secciones.objects.get(id_seccion=id_seccion)
    return render(request, 'CRUD_tareas/Crear_tarea.html',{"seccion":seccion})

@login_required
def crear_tarea(request, id_seccion):
    seccion = Secciones.objects.get(id_seccion=id_seccion)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']

        Tareas.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            id_seccion=seccion,
            tipo_tablero=1
        )
        messages.success(request, 'Tarea creada con exito')
        return redirect('CRUD_tareas',id_seccion)
    messages.error(request, 'La tarea no creada')
    return redirect('crear_tarea_view',id_seccion)

@login_required
def editar_tarea_view(request, id_tarea):
    tarea = Tareas.objects.get(id_tarea=id_tarea)
    return render(request, 'CRUD_tareas/Editar_tarea.html',{'tarea': tarea})

@login_required
def editar_tarea(request, id_tarea):
    tarea = Tareas.objects.get(id_tarea=id_tarea)
    if request.method == 'POST':
        tarea.nombre = request.POST['nombre']
        tarea.descripcion = request.POST['descripcion']
        tarea.save()
        messages.success(request, 'Tarea editada con exito')
        return redirect('CRUD_tareas',tarea.id_seccion.id_seccion)
    messages.error(request, 'La tarea no editada')
    return redirect('editar_tarea_view', id_tarea)

@login_required
def eliminar_tarea(request, id_tarea):
    tarea = Tareas.objects.get(id_tarea=id_tarea)
    tarea.delete()
    messages.success(request, 'Tarea eliminada con exito')
    return redirect('CRUD_tareas',tarea.id_seccion.id_seccion)
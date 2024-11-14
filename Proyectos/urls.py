from django.urls import path
from . import views

urlpatterns = [
    # CRUD proyectos
    path('proyectos/<user>', views.CRUD_proyectos, name='CRUD_proyectos'),
    path('crear_proyecto_view/', views.crear_proyecto_view, name='crear_proyecto_view'),
    path('crear_proyecto/<user>/', views.crear_proyecto, name='crear_proyecto'),
    path('editar_proyecto_view/<id_proyecto>', views.editar_proyecto_view, name='editar_proyecto_view'),
    path('editar_proyecto/<id_proyecto>', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto/<id_proyecto>', views.eliminar_proyecto, name='eliminar_proyecto'),

    # CRUD secciones
    path('secciones/<id_proyecto>', views.CRUD_secciones, name='CRUD_secciones'),
    path('crear_seccion/<id_proyecto>', views.crear_seccion, name='crear_seccion'),
    path('editar_seccion_view/<id_seccion>', views.editar_seccion_view, name='editar_seccion_view'),
    path('editar_seccion/<id_seccion>', views.editar_seccion, name='editar_seccion'),
    path('eliminar_seccion/<id_seccion>', views.eliminar_seccion, name='eliminar_seccion'),

    # CRUD tareas
    path('tareas/<id_seccion>', views.CRUD_tareas, name='CRUD_tareas'),
    path('crear_tarea_view/<id_seccion>', views.crear_tarea_view, name='crear_tarea_view'),
    path('crear_tarea/<id_seccion>', views.crear_tarea, name='crear_tarea'),
    path('editar_tarea_view/<id_tarea>', views.editar_tarea_view, name='editar_tarea_view'),
    path('editar_tarea/<id_tarea>', views.editar_tarea, name='editar_tarea'),
    path('eliminar_tarea/<id_tarea>', views.eliminar_tarea, name='eliminar_tarea'),
]
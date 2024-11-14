from django.urls import path
from . import views

urlpatterns = [
    # Login
    path('iniciar_sesion/', views.login_view, name='login_view'),
    path('iniciar_sesion2/', views.iniciar_sesion, name='login'),
    # Logout
    path('cerrar_sesion/', views.cerrar_sesion, name='logout'),
    # Register
    path('registrarse/', views.register_view, name='register_view'),
    path('registrarse2/', views.registrarse, name='registrarse'),
    # CRUD usuarios
    path('usuarios/',views.CRUD_usuarios, name='CRUD_usuarios'),
    path('editar_usuario/<user>',views.editar_usuario, name='editar_usuario'),
    path('editar_usuario2/<user>',views.editar_usuario2, name='editar_usuario2'),
    path('eliminar_usuario/<user>',views.eliminar_usuario, name='eliminar_usuario'),
]

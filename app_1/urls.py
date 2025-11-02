"""
Configuración de URLs para la aplicación app_1
Conecta las vistas con las rutas URL siguiendo el patrón MTV
"""
from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Autenticación
    path('login/', views.inicio_sesion, name='login'),
    path('signin/', views.inicio_sesion, name='signin'),  # Alias para /signin
    path('logout/', views.cerrar_sesion, name='logout'),

    # Dashboard (requiere autenticación)
    path('dashboard/', views.dashboard, name='dashboard'),

    # Páginas informativas
    path('conocenos/', views.conocenos, name='conocenos'),
    path('catalogo/', views.catalogo, name='catalogo'),
]
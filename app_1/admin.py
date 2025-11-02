"""
Configuración del panel de administración de Django para app_1
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Administrador personalizado para el modelo CustomUser
    Extiende UserAdmin de Django para incluir campos personalizados
    """
    # Campos a mostrar en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'email_verified', 'terms_accepted')

    # Campos por los que se puede filtrar
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'email_verified', 'terms_accepted', 'date_joined')

    # Campos de búsqueda
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Orden predeterminado
    ordering = ('-date_joined',)

    # Configuración de fieldsets para el formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('email_verified', 'terms_accepted', 'phone'),
        }),
    )

    # Configuración de fieldsets para el formulario de creación
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {
            'fields': ('email', 'email_verified', 'terms_accepted', 'phone'),
        }),
    )

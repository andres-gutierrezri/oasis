"""
Vistas de la aplicación app_1
Implementa el patrón MTV (Modelo-Template-Vista) de Django
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import CustomUser


# Vista principal (página de inicio)
def index(request):
    """
    Vista de la página de inicio/home
    Template: app_1/index.html
    """
    return render(request, 'app_1/index.html')


# Vista de inicio de sesión y registro
@require_http_methods(["GET", "POST"])
def inicio_sesion(request):
    """
    Vista combinada para login y registro de usuarios
    Template: app_1/incio_de_sesion.html (nota el typo en el nombre del archivo)
    """
    if request.method == 'POST':
        # Determinar si es login o registro según el campo presente
        if 'loginEmail' in request.POST:
            # Proceso de Login
            email = request.POST.get('loginEmail')
            password = request.POST.get('loginPassword')

            # Autenticar usuario
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido a OASIS, {user.first_name or user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Correo o contraseña incorrectos')

        elif 'regEmail' in request.POST:
            # Proceso de Registro
            name = request.POST.get('regName')
            email = request.POST.get('regEmail')
            password = request.POST.get('regPassword')
            confirm = request.POST.get('regConfirm')

            # Validaciones
            if password != confirm:
                messages.error(request, 'Las contraseñas no coinciden')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Ese correo ya está registrado')
            else:
                # Crear usuario
                try:
                    # Separar nombre en first_name y last_name
                    name_parts = name.split(' ', 1)
                    first_name = name_parts[0]
                    last_name = name_parts[1] if len(name_parts) > 1 else ''

                    user = CustomUser.objects.create_user(
                        username=email,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        terms_accepted=True
                    )
                    messages.success(request, 'Cuenta creada con éxito. Ahora puedes iniciar sesión.')
                except Exception as e:
                    messages.error(request, f'Error al crear cuenta: {str(e)}')

    return render(request, 'app_1/incio_de_sesion.html')


# Vista de cerrar sesión
def cerrar_sesion(request):
    """
    Vista para cerrar sesión del usuario
    Redirige a la página de inicio
    """
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente')
    return redirect('index')


# Vista del dashboard (requiere autenticación)
@login_required
def dashboard(request):
    """
    Vista del panel de control del usuario
    Requiere que el usuario esté autenticado
    """
    context = {
        'user': request.user
    }
    return render(request, 'app_1/dashboard.html', context)


# Vista de la página "Conócenos"
def conocenos(request):
    """
    Vista de la página informativa "Conócenos"
    Template: app_1/conocenos.html
    """
    return render(request, 'app_1/conocenos.html')


# Vista del catálogo
def catalogo(request):
    """
    Vista del catálogo de productos/servicios
    Template: app_1/catalogo.html
    """
    return render(request, 'app_1/catalogo.html')

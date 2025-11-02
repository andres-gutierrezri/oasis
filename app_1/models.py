from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de usuario personalizado
class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser de Django
    Añade campos adicionales para verificación de email y aceptación de términos
    """
    email = models.EmailField('Correo electrónico', unique=True)
    email_verified = models.BooleanField('Email verificado', default=False)
    terms_accepted = models.BooleanField('Términos aceptados', default=False)

    # Campos opcionales adicionales
    phone = models.CharField('Teléfono', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email or self.username

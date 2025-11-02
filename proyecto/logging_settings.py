import os
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv()

# Variable para determinar si estamos en producción
IS_DEPLOYED = os.getenv("IS_DEPLOYED", "False") == "True"

# Configuración base de logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] %(name)s %(funcName)s:%(lineno)d - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO" if IS_DEPLOYED else "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO" if IS_DEPLOYED else "DEBUG",
            "propagate": False,
        },
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# En desarrollo local, agregar handler de archivo si el directorio existe
if not IS_DEPLOYED:
    # Crear directorio tmp si no existe
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tmp")
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError:
            pass  # Si no se puede crear, no pasa nada
    
    # Solo agregar file handler si el directorio existe
    if os.path.exists(log_dir):
        LOGGING["handlers"]["file"] = {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(log_dir, "django.log"),
            "formatter": "verbose",
        }
        # Agregar el handler de archivo a los loggers
        LOGGING["loggers"]["django"]["handlers"].append("file")

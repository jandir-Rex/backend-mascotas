import dj_database_url
import pymysql
import os
from pathlib import Path

# Configurar pymysql como el conector de MySQL nativo
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l5o^w6@8*z@w!pu3or9lay@85op4pakede(^xg!ghk)50kj$)n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Hosts permitidos para producción local y en el servidor Render
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',  # Requisito obligatorio antes de staticfiles para multimedia
    'django.contrib.staticfiles',
    'cloudinary',          # App de Cloudinary para gestionar las subidas
    'rest_framework',
    'corsheaders',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # SIEMPRE EN PRIMER LUGAR PARA EVITAR BLOQUEOS CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_mascotas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_mascotas.wsgi.application'


# Database
# Configuración directa con la base de datos MySQL de Aiven en Internet

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Configuración obligatoria de SSL seguro requerido por Aiven
DATABASES['default']['OPTIONS'] = {
    'ssl': {
        'ssl_mode': 'REQUIRED'
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# Configuración de estáticos lista para despliegues en producción (Render)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración para archivos multimedia remotos (Imágenes de mascotas)
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Configuración del almacenamiento global (Django 4.2+)
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Permitir orígenes cruzados en Internet (Conexión directa con Vercel)
CORS_ALLOW_ALL_ORIGINS = True


# Credenciales de Cloudinary vinculadas con tu cuenta a través de variables de entorno
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'dnoxmbt8c'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '128522478898481'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', 'PYjYRGus1gWbvmXZ73r0Mpofl4Q'),
}
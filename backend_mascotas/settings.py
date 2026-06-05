import dj_database_url
import pymysql
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (funciona local y no afecta Render)
load_dotenv()

# Configurar pymysql como el conector de MySQL nativo
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


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
    'cloudinary_storage',  # Obligatorio ANTES de staticfiles
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'corsheaders',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # SIEMPRE PRIMERO
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


# ---------------------------------------------------------------
# BASE DE DATOS — MySQL en Railway via DATABASE_URL
# ---------------------------------------------------------------
_db_url = os.environ.get('DATABASE_URL')

if _db_url:
    DATABASES = {
        'default': dj_database_url.config(
            default=_db_url,
            conn_max_age=600
        )
    }
else:
    import warnings
    warnings.warn("No DATABASE_URL encontrado. Usando base de datos SQLite local.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db_local_fallback.sqlite3',
        }
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------------
# ARCHIVOS ESTÁTICOS
# ---------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# ---------------------------------------------------------------
# ARCHIVOS MULTIMEDIA — Cloudinary
# ---------------------------------------------------------------
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}


# ---------------------------------------------------------------
# CORS — Permite peticiones desde Vercel
# ---------------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True


# ---------------------------------------------------------------
# CLOUDINARY — Credenciales via variables de entorno
# ---------------------------------------------------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'dnoxmbt8c'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '128522478898481'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', 'PYjYRGus1gWbvmXZ73r0Mpofl4Q'),
}


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
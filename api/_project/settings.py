from pathlib import Path
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-yh%834@2g(m41!fw480_n7gxvb6wm9ovnx&#zn_1z4atpba^wn'

DEBUG = int(os.environ.get("DEBUG"))

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['api.' + os.environ.get("DOMAIN"), 'api']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local
    'users',
    'recipes',
    # 3rd party
    'rest_framework',
    'django_rest_passwordreset',
    'corsheaders',
    'storages',
    'django_cleanup',   #need to be last
]

AUTH_USER_MODEL = 'users.CustomUser'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

EMAIL_BACKENDS = 'django.core.mail.backends.console.EmailBackend'
### To use email, replace the variables below with your email provider info
# EMAIL_BACKENDS = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = <your email>
# EMAIL_HOST_PASSWORD = <your password>
# EMAIL_PORT = 587 #for gmail only
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = <your email>

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', #need to be first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #need to be above all but security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = ["https://" + os.environ.get("DOMAIN")]

ROOT_URLCONF = '_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '_project.wsgi.application'

if bool(int(os.environ.get('USE_RDS'))):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('RDS_NAME'),
            'USER': os.environ.get('RDS_USER'),
            'PASSWORD': os.environ.get('RDS_PASSWORD'),
            'HOST': os.environ.get('RDS_HOST'),
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')

MEDIA_URL = '/api/media/'
if bool(int(os.environ.get('USE_S3'))):
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_ACCESS_SECRET')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_BUCKET_REGION')
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_FILE_OVERWRITE = False
    AWS_S3_ADDRESSING_STYLE = 'virtual'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media').replace('\\', '/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

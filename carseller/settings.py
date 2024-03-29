"""
Django settings for carseller project.

"""

import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['misspowershow.onrender.com', '127.0.0.1/admin', '127.0.0.1', 'localhost']

SITE_ID = 2

SERVER_HEADER = None


INTERNAL_IPS = [
    # ...
    '127.0.0.1',
]

WHITENOISE_SKIP_COMPRESS = True

DOMAIN = 'http://127.0.0.1:8001/'
LOGIN_REDIRECT_URL = 'admin:index'

AUTH_USER_MODEL = 'admin_registration.AdminUser'

# Application definition

INSTALLED_APPS = [
    # 'csp',
    'jazzmin',
    'admin_registration',
    'message',
    'whitenoise.runserver_nostatic',
    'accounts.apps.AccountsConfig',
    'cars.apps.CarsConfig',
    'contacts.apps.ContactsConfig',
    'pages.apps.PagesConfig',
    'inquiry.apps.InquiryConfig',
    'brands.apps.BrandsConfig',
    'our_products.apps.OurProductsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'ckeditor',
    'django.contrib.humanize',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'carseller.middlewares.HideServerMiddleware',
    # 'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 86400  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

X_FRAME_OPTIONS = 'DENY'

ROOT_URLCONF = 'carseller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'carseller.wsgi.application'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_directory'),
    }
}

# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv('DATABASE_URL', 'carwebsite-instances.cre2ic6gofxe.us-west-2.rds.amazonaws.com')
#     )
# }
#         'ENGINE': 'djongo',
# DATABASES = {
#     'default': {
#         'NAME': 'carwebsite',
#         # 'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#             'host': 'localhost',
#             'port': 27017,  # MongoDB default port
#             'username': 'blockbuster045',
#             'password': 'ThgRs5yqkLOJ1vMu',
#             # 'authSource': 'admin',
#             # 'authMechanism': 'SCRAM-SHA-1',
#         }
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carwebsite',
        'USER': 'postgres',
        'PASSWORD': 'bumblebee47',
        'HOST': 'carwebsite-instances.cre2ic6gofxe.us-west-2.rds.amazonaws.com',  # Your AWS RDS endpoint
        'PORT': '5432',  # Default PostgreSQL port
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Development Settings
if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

# Production Settings
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


AWS_ACCESS_KEY_ID = 'AKIAYVAQR36KDQSCENST'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'django-carwebsite'
AWS_S3_REGION_NAME = 'us-west-2'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = ('SG.IqUx_NnGTlqw3dixtptlZg.'
                       'Knl6iSv-JrX3t1j7FJync7ohlqirkpjVGnLBzoAoYR0')

# Additional SendGrid settings
SENDGRID_SANDBOX_MODE_IN_DEBUG = True

# Additional setting for SMTP debugging
EMAIL_DEBUG = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'core.storages.MediaStore'

JAZZMIN_SETTINGS = {
    # "site_logo_classes": "img-square",

    "site_logo": "img/logos/newlogo-removebg-preview.png",

    # # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "miss power",

    # # Title on the login screen (19 chars max)
    "site_header": "",

    "site_brand": "M.POWER",

    'custom_css': "jazzmin_custom/custom_admin_base.html",

    "welcome_sign": "Welcome Django Admin ",

    "search_model": ["auth.User", "auth.Group"],

    "login_logo": "img/logos/newlogo-removebg-preview.png",


    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
    ],

}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    # ...
    'allauth.account.auth_backends.AuthenticationBackend',
    # ...
]


ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


# # Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 86400  # 1 day in seconds
SESSION_COOKIE_NAME = 'car_website'
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True
#
# # # Disable the Server information in the HTTP response header
SECURE_SERVER_HEADERS = True

# Development Settings
if DEBUG:
    SECURE_SSL_REDIRECT = False

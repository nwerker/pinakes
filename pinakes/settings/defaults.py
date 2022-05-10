"""
Django settings for pinakes project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import environ
import os
import sys
from pathlib import Path


env = environ.Env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Django gettext files path:
# locale/<lang-code>/LC_MESSAGES/django.po, django.mo
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("PINAKES_DEBUG", default=False)
TEMPLATE_DEBUG = DEBUG
SQL_DEBUG = DEBUG
SECRET_KEY = env.str("PINAKES_SECRET_KEY")

ALLOWED_HOSTS = env.list(
    "PINAKES_ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1"],
)

CATALOG_API_PATH_PREFIX = env.str(
    "PINAKES_API_PATH_PREFIX",
    default="/api/pinakes",
)

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
    "rest_framework",
    "django_filters",
    "rest_framework.authtoken",
    "taggit",
    "django_rq",
    "drf_spectacular",
    "social_django",
    "corsheaders",
    "pinakes.main",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "pinakes.common.auth.middleware.KeycloakAuthMiddleware",
]

ROOT_URLCONF = "pinakes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "pinakes.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("PINAKES_DATABASE_NAME", default="catalog"),
        "USER": env.str("PINAKES_POSTGRES_USER", default="catalog"),
        "PASSWORD": env.str("PINAKES_POSTGRES_PASSWORD", default="password"),
        "HOST": env.str("PINAKES_POSTGRES_HOST", default="localhost"),
        "PORT": env.str("PINAKES_POSTGRES_PORT", default="5432"),
        "OPTIONS": {
            "sslmode": env.str("PINAKES_POSTGRES_SSL_MODE", default="require"),
            "sslcert": env.str("PINAKES_POSTGRES_SSL_CERT", default=""),
            "sslkey": env.str("PINAKES_POSTGRES_SSL_KEY", default=""),
            "sslrootcert": env.str(
                "PINAKES_POSTGRES_SSL_ROOT_CERT", default=""
            ),
        },
    }
}

# REST Framework configuration
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": (
        "pinakes.common.pagination.CatalogPageNumberPagination"
    ),
    "PAGE_SIZE": 25,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": (
        "pinakes.common.exception_handler.custom_exception_handler"
    ),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]

AUTHENTICATION_BACKENDS = [
    "pinakes.common.auth.keycloak_oidc.KeycloakOpenIdConnect",
    "django.contrib.auth.backends.ModelBackend",
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/ui/"
STATICFILES_DIRS = [
    BASE_DIR / "ui",
]
STATIC_ROOT = env.str("PINAKES_STATIC_ROOT", default=BASE_DIR / "staticfiles")
LOGIN_REDIRECT_URL = env.str(
    "PINAKES_LOGIN_REDIRECT_URL",
    default="/ui/catalog/index.html",
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Controller Info
CONTROLLER_URL = env.str(
    "PINAKES_CONTROLLER_URL",
    default="https://Your_Controller_URL",
)
CONTROLLER_TOKEN = env.str("PINAKES_CONTROLLER_TOKEN", default="Secret Token")
CONTROLLER_VERIFY_SSL = env.str(
    "PINAKES_CONTROLLER_VERIFY_SSL", default="True"
)

# Media (Icons) configuration
MEDIA_ROOT = env.str(
    "PINAKES_MEDIA_ROOT",
    default=BASE_DIR / "media",
)
MEDIA_URL = "/media/"

if "pytest" in sys.modules:
    MEDIA_ROOT = os.path.join(BASE_DIR, "main/catalog/tests/data/")

# Logging configuration
LOG_LEVEL = "DEBUG" if DEBUG else env.str("DJANGO_LOG_LEVEL", "INFO")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "[{asctime}] [{process:d}] [{levelname}] {module} {thread:d}"
                " {message}"
            ),
            "style": "{",
        },
        "simple": {
            "format": "%(asctime)s — %(name)s — %(levelname)s — %(message)s",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "rq_console": {
            "level": LOG_LEVEL,
            "class": "rq.utils.ColorizingStreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
        },
        "pinakes": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "analytics": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "approval": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "catalog": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "inventory": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "rq.worker": {
            "handlers": ["rq_console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}

LOGIN_URL = "/login/keycloak/"

# Django Redis Queue Information
if "PINAKES_REDIS_UNIX_SOCKET_PATH" in env:
    RQ_QUEUES = {
        "default": {
            "UNIX_SOCKET_PATH": env.str("PINAKES_REDIS_UNIX_SOCKET_PATH"),
        },
    }
else:
    RQ_QUEUES = {
        "default": {
            "HOST": env.str("PINAKES_REDIS_HOST", default="localhost"),
            "PORT": env.int("PINAKES_REDIS_PORT", default=6379),
        },
    }

RQ_QUEUES["default"]["DB"] = env.int("PINAKES_REDIS_DB", default=0)
RQ_QUEUES["default"]["DEFAULT_TIMEOUT"] = 360

# RQ Cron Jobs setting
STARTUP_RQ_JOBS = [
    "pinakes.main.common.tasks.sync_external_groups",
    "pinakes.main.inventory.tasks.refresh_all_sources",
]
CRONTAB = env.str("PINAKES_CRONTAB", default="*/30 * * * *")
RQ_CRONJOBS = [
    (
        CRONTAB,
        "pinakes.main.common.tasks.sync_external_groups",
    ),
    (
        CRONTAB,
        "pinakes.main.inventory.tasks.refresh_all_sources",
    ),
    (
        "* 0 * * *",
        "pinakes.main.common.tasks.clear_sessions",
    ),
]

# Auto generation of openapi spec using Spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "Catalog API",
    "DESCRIPTION": (
        "A set of APIs to create and manage Ansible catalogs and order from"
        " them."
    ),
    "VERSION": "0.1.0",
    "CONTACT": {
        "email": "support@redhat.com",
    },
    "LICENSE": {
        "name": "Apache 2.0",
        "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
    },
    "SERVERS": [
        {
            "url": "{scheme}://{host}:{port}/{basePath}",
            "description": "Development Server",
            "variables": {
                "scheme": {
                    "default": "http",
                },
                "host": {
                    "default": "localhost",
                },
                "port": {
                    "default": "8000",
                },
                "basePath": {
                    "default": "",
                },
            },
        },
    ],
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX": "/{}/v1".format(CATALOG_API_PATH_PREFIX.strip("/")),
}

SOCIAL_AUTH_JSONFIELD_ENABLED = True

KEYCLOAK_URL = env.str(
    "PINAKES_KEYCLOAK_URL",
    default="http://localhost:8080/auth",
).rstrip("/")
KEYCLOAK_REALM = env.str("PINAKES_KEYCLOAK_REALM", default="pinakes")
KEYCLOAK_CLIENT_ID = env.str("PINAKES_KEYCLOAK_CLIENT_ID", default="pinakes")
KEYCLOAK_CLIENT_SECRET = env.str(
    "PINAKES_KEYCLOAK_CLIENT_SECRET",
    default="secret-token",
)

KEYCLOAK_VERIFY_SSL = env.bool("PINAKES_KEYCLOAK_VERIFY_SSL", True)
if KEYCLOAK_VERIFY_SSL:
    KEYCLOAK_VERIFY_SSL = env.str(
        "PINAKES_KEYCLOAK_CA_PATH", KEYCLOAK_VERIFY_SSL
    )

SOCIAL_AUTH_KEYCLOAK_OIDC_KEY = KEYCLOAK_CLIENT_ID
SOCIAL_AUTH_KEYCLOAK_OIDC_API_URL = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}"
SOCIAL_AUTH_KEYCLOAK_OIDC_SECRET = KEYCLOAK_CLIENT_SECRET

SOCIAL_AUTH_KEYCLOAK_OIDC_VERIFY_SSL = KEYCLOAK_VERIFY_SSL
SOCIAL_AUTH_REDIRECT_IS_HTTPS = env.bool(
    "PINAKES_HTTPS_ENABLED", default=False
)
# CORS
# Comma separated values list of :"SCHEME+HOST+[PORT]", e.g.
# PINAKES_UI_ALLOWED_ORIGINS = \
#   "https://example.com,https://catalog.example.com:9090"
CORS_ALLOWED_ORIGINS = env.list("PINAKES_UI_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = False
CSRF_TRUSTED_ORIGINS = env.list("PINAKES_CSRF_TRUSTED_ORIGINS", default=[])
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Metrics collections
PINAKES_INSIGHTS_TRACKING_STATE = env.bool(
    "PINAKES_INSIGHTS_TRACKING_STATE", False
)
PINAKES_INSIGHTS_AUTH_METHOD = env.str(
    "PINAKES_INSIGHTS_AUTH_METHOD",
    default="certificate",
)

if PINAKES_INSIGHTS_AUTH_METHOD == "certificate":
    PINAKES_INSIGHTS_URL = env.str(
        "PINAKES_INSIGHTS_URL",
        default="https://cert.cloud.redhat.com/api/ingress/v1/upload",
    )
else:
    PINAKES_INSIGHTS_URL = env.str(
        "PINAKES_INSIGHTS_URL",
        default="https://cloud.redhat.com/api/ingress/v1/upload",
    )
    PINAKES_INSIGHTS_USERNAME = env.str(
        "PINAKES_INSIGHTS_USERNAME",
        default="unknown",
    )
    PINAKES_INSIGHTS_PASSWORD = env.str(
        "PINAKES_INSIGHTS_PASSWORD",
        default="unknown",
    )

if PINAKES_INSIGHTS_TRACKING_STATE:
    STARTUP_RQ_JOBS.append(
        "pinakes.main.analytics.tasks.gather_analytics",
    )
    RQ_CRONJOBS.append(
        (
            "5 0 * * 0",  # At 00:05 on Sunday
            "pinakes.main.analytics.tasks.gather_analytics",
        ),
    )

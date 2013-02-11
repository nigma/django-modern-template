#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
INTERNAL_IPS = ["127.0.0.1"]

SECRET_KEY = "dummy"

DOMAIN_NAME = "{{ project_name }}.dev"
SITE_NAME = "{{ project_name }} (dev)"

DEFAULT_FROM_EMAIL = "{} <hey@{}>".format(SITE_NAME, DOMAIN_NAME)
SERVER_EMAIL = "server@{}".format(DOMAIN_NAME)
EMAIL_SUBJECT_PREFIX = "[{} (dev)]".format(SITE_NAME)

# Static and media files
STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = rel("..", "media").replace("\\", "/")

# DATABASE, CACHE AND EMAIL BACKENDS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "{{ project_name }}",
        "USER": "{{ project_name }}",
        "PASSWORD": "pass",
        "OPTIONS": {
            "autocommit": True,
        }
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache"
    },
    "locmem": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    },
    "dummy": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# WARNING: enabling debug toolbar breaks nested transaction/savepoint recovery
# with error: `InternalError: current transaction is aborted, commands ignored
# until end of transaction blocks`

MIDDLEWARE_CLASSES += ["debug_toolbar.middleware.DebugToolbarMiddleware",]
INSTALLED_APPS += ["debug_toolbar",]

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "HIDE_DJANGO_SQL": False,
    "ENABLE_STACKTRACES": True
}

DEBUG_TOOLBAR_PANELS = [
    #"debug_toolbar.panels.version.VersionDebugPanel",
    "debug_toolbar.panels.timer.TimerDebugPanel",
    "debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel",
    "debug_toolbar.panels.headers.HeaderDebugPanel",
    "debug_toolbar.panels.request_vars.RequestVarsDebugPanel",
    #"debug_toolbar.panels.template.TemplateDebugPanel",
    "debug_toolbar.panels.sql.SQLDebugPanel",
    "debug_toolbar.panels.signals.SignalDebugPanel",
    "debug_toolbar.panels.logger.LoggingPanel",
    "debug_toolbar.panels.cache.CacheDebugPanel",
    #"debug_toolbar.panels.profiling.ProfilingDebugPanel"
]

COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter"
]
COMPRESS_JS_FILTERS = []
COMPRESS_CACHE_BACKEND = "dummy"

CRISPY_FAIL_SILENTLY = False

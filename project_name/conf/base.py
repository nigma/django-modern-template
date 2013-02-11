# -*- coding: utf-8 -*-
# Refer to https://docs.djangoproject.com/en/dev/ref/settings/ for docs

from __future__ import unicode_literals

import site
from . import rel, get_env_setting
site.addpackage(rel(), "apps.pth", known_paths=set())

DEBUG = False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = rel("..", "static_collected")

STATICFILES_DIRS = [
    rel("static")
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    # "django.template.loaders.eggs.Loader",
]

TEMPLATE_DIRS = [
    rel("templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    "account.context_processors.account",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    #"django.middleware.http.ConditionalGetMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware", # Cookie-based, for anonymous users
    "account.middleware.LocaleMiddleware", # Account-based, for registered users
    "account.middleware.TimezoneMiddleware",
]

INSTALLED_APPS = [
    # Django apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.admin",

    # Pinax user accounts apps
    "account",
    "pinax_theme_bootstrap_account",
    "django_forms_bootstrap", # TODO: bootstrap/field.html template collides with crispy-forms

    # Top utilities for assets management, db migrations, api and more
    "compressor",
    "crispy_forms",
    "django_extensions",
    "infinite_pagination",
    #"imagekit",
    "rest_framework",
    "south",
    "storages",

    # Project apps
    "about",
    "api",
    "core",
    "home",
    "util",
]

WSGI_APPLICATION = "wsgi.application"

ROOT_URLCONF = "{{ project_name}}.urls"

SESSION_STORAGE = "django.contrib.sessions.backends.cached_db"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTH_USER_MODEL = "auth.User"

AUTHENTICATION_BACKENDS = [
    "account.auth_backends.EmailAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Common app-specific settings

from .common.account import *
from .common.compress import *
from .common.imagekit import *
from .common.logs import LOGGING

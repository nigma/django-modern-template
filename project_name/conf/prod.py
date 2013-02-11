#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from .base import *

# Settings read from Heroku env (see https://github.com/nigma/django-herokuify)
import herokuify
from herokuify.common import *
from herokuify.aws import *
from herokuify.mail.mailgun import *

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = get_env_setting("DJANGO_SECRET_KEY")

ADMINS = [
    # ('Your Name', 'your_email@example.com'),
]

# Configure site name and domain
DOMAIN_NAME = "{{ project_name }}.example.net"
SITE_NAME = "{{ project_name|title }}"

DEFAULT_FROM_EMAIL = "{} <hey@{}>".format(SITE_NAME, DOMAIN_NAME)
SERVER_EMAIL = "server@{}".format(DOMAIN_NAME)
EMAIL_SUBJECT_PREFIX = "[{}]".format(SITE_NAME)

# Database and cache settings
DATABASES = herokuify.get_db_config()
CACHES = herokuify.get_cache_config()

# Setup storage for static files and media using S3 Boto backend
DEFAULT_FILE_STORAGE = "herokuify.storage.S3MediaStorage"
STATICFILES_STORAGE = "herokuify.storage.CachedS3StaticStorage"
COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"

MEDIA_URL = "https://{0}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)
STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

# Compress assets during deployment
COMPRESS_OFFLINE = True

# Enable caching for templates
TEMPLATE_LOADERS = [
    ("django.template.loaders.cached.Loader", TEMPLATE_LOADERS),
]

# Enable postgres connection pool
DATABASES['default']['ENGINE'] = 'django_postgrespool'
DATABASE_POOL_ARGS = {
    'max_overflow': 10,
    'pool_size': 10,
    'recycle': 300
}
SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}

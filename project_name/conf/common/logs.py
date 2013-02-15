#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import logging

logging.captureWarnings(True)

catch_all_handlers = ["console"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S"
        },
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s [%(name)s:%(lineno)s] %(process)d %(thread)d %(message)s"
        },
        "console": {
            "format": "[%(asctime)s] %(levelname)5s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%H:%M:%S"
        }
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": False,
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "console",
            "stream": sys.stdout
        },
    },
    "loggers": {
        "": {
            "handlers": catch_all_handlers,
            "level": "DEBUG",
        },
        "boto": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.startup": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR"
        },
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": [],
            "propagate": False,
        },
        "django.commands": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "app": {
            "handlers": ["console"],
            "level": "INFO"
        }
    }
}

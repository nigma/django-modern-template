# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

from django.conf import settings
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule

logger = logging.getLogger("django.startup")


def autoload(submodules):
    """
    :param list submodules: List of app submodules to import
    """
    for app in settings.INSTALLED_APPS:

        try:
            mod = import_module(app)
        except Exception:
            logger.exception("Application module import failed: %s", app)
            raise

        for submodule in submodules:
            module_name = "{}.{}".format(app, submodule)
            logger.debug("Importing module: %s", module_name)

            try:
                import_module(module_name)
            except Exception:
                if module_has_submodule(mod, submodule):
                    logger.exception("Module import failed: %s", module_name)
                    raise
                else:
                    logger.debug("Module not present: %s", module_name)
            else:
                logger.info("Loaded module: %s", module_name)


def run():
    autoload(["receivers"])

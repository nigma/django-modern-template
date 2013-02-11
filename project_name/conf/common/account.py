#-*- coding: utf-8 -*-

# Settings for django-user-accounts (https://github.com/pinax/django-user-accounts)

ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_login"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_USER_DISPLAY = lambda user: user.get_full_name() or user.email

THEME_ACCOUNT_CONTACT_EMAIL = "info@{{ domain_name }}"

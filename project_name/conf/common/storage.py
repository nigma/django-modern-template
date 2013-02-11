#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import time

from django.utils.http import http_date

# AWS access settings for S3 Boto storage
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
AWS_S3_FILE_OVERWRITE = True
AWS_HEADERS = {
    "Expires": http_date(
        time.mktime((datetime.datetime(2020, 12, 31)).timetuple())),
    "Cache-Control": "max-age=%d" % (365 * 24 * 60 * 60),
}

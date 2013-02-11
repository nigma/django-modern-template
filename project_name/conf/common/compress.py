#-*- coding: utf-8 -*-

# Settings for Django Compressor (https://github.com/jezdez/django_compressor)

from __future__ import unicode_literals

COMPRESS_PRECOMPILERS = [
    ("text/coffeescript", "coffee --compile --stdio"),
    ("text/less", "lessc {infile}"),
    ("text/x-sass", "sass {infile} {outfile}"),
    ("text/x-scss", "sass --scss {infile} {outfile}"),
]

COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter"
]

COMPRESS_JS_FILTERS = [
    "compressor.filters.jsmin.JSMinFilter"
]

COMPRESS_OUTPUT_DIR = "cache"

COMPRESS_CACHE_BACKEND = "locmem"

COMPRESS_ENABLED = True

COMPRESS_PARSER = "compressor.parser.default_htmlparser.DefaultHtmlParser"

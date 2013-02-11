#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.sitemaps import Sitemap


class AboutSitemap(Sitemap):

    def __init__(self, base_url="/about/"):
        self.base_url = base_url

    def items(self):
        urls = [
           "",
           "terms/",
           "privacy/",
        ]
        return [{"location": self.base_url + url} for url in urls]

    def location(self, obj):
        return obj["location"]

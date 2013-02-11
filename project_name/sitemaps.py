#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.sitemaps import GenericSitemap

from about.sitemaps import AboutSitemap

#class SampleSitemap(GenericSitemap):
#    info_dict = {"queryset": Model.objects.all(), "date_field": "modified_at"}
#    changefreq = "week"
#    priority = 0.6
#
#    def __init__(self):
#        super(SampleSitemap, self).__init__(
#           self.info_dict, self.priority, self.changefreq)


sitemaps = {
    "about": AboutSitemap(),
}

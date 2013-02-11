#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="about/about.html"), name="about"),
    url(r"^terms/$", TemplateView.as_view(template_name="about/terms.html"), name="terms"),
    url(r"^privacy/$", TemplateView.as_view(template_name="about/privacy.html"), name="privacy"),
)

#-*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from sitemaps import sitemaps

#handler500 = "util.views.server_error"

admin.autodiscover()

urlpatterns = patterns("",
    url(r"^$",          include("home.urls")),
    url(r"^about/",     include("about.urls", namespace="about")),
    url(r"^account/", include("account.urls")),
    url(r"^api/", include("api.urls")),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^sitemap\.xml$", "django.contrib.sitemaps.views.sitemap", kwargs={"sitemaps": sitemaps}),
    url(r"^admin/", include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

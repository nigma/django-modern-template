#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView, DetailView


class IndexView(TemplateView):
    template_name = "home/index.html"


class HomepageView(DetailView):
    template_name = "home/homepage.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user

index = IndexView.as_view()
homepage = HomepageView.as_view()


def select_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return homepage(request, *args, **kwargs)
    return index(request, *args, **kwargs)

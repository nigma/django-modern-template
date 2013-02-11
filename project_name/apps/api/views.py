#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class ApiRoot(APIView):
    """
    The root view for the rest api.
    """

    permissions = (IsAuthenticated, )

    def build_url(self, request, urlname):
        if isinstance(urlname, dict):
            return reverse(request=request, **urlname)
        return reverse(urlname, request=request)

    def get(self, request):
        data = [{
            "name": name,
            "url": self.build_url(request, urlname)
        } for name, urlname in [
            # ("Object list", "api_object_list"),
        ]]
        return Response(data)

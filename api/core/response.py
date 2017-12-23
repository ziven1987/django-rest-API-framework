# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

__author__ = 'ziven'

from rest_framework.response import Response


def success(data):
    return Response({'code': 200, 'data': data})


def error(code, msg):
    return Response({'code': code, 'msg': msg})


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

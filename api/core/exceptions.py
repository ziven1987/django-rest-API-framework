# -*- coding: utf-8 -*-
from django.utils import six

from rest_framework.exceptions import APIException

__author__ = 'ziven'


class APIError(APIException):
    def __init__(self, detail, code=406):
        self.status_code = code
        self.detail = detail

    def __str__(self):
        return six.text_type(self.detail)

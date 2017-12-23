# -*- coding: utf-8 -*-
import rest_framework_swagger
from django.apps import AppConfig
from . import introspectors

__author__ = 'ziven'


class Config(AppConfig):
    name = 'api.core'
    label = 'core'


default_app_config = 'api.core.Config'


def patch():
    rest_framework_swagger.introspectors.APIViewMethodIntrospector = \
        introspectors.APIViewMethodIntrospector
    rest_framework_swagger.introspectors.WrappedAPIViewMethodIntrospector = \
        introspectors.WrappedAPIViewMethodIntrospector

patch()

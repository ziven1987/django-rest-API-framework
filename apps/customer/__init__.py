# -*- coding: utf-8 -*-

from django.apps import AppConfig


class Config(AppConfig):
    label = 'customer'
    name = 'apps.customer'

default_app_config = 'apps.customer.Config'

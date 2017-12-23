# -*- coding: utf-8 -*-

import logging
import sys
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.compat import set_rollback
from .response import error

__author__ = 'ziven'

logger = logging.getLogger('django.request')


def exception_handler(exc, context):
    if isinstance(exc, exceptions.ValidationError):
        set_rollback()
        return error(exc.status_code, exc.detail)
    elif isinstance(exc, Http404):
        msg = 'Not found.'
        set_rollback()
        return error(404, msg)
    elif isinstance(exc, PermissionDenied):
        msg = 'Permission denied.'
        set_rollback()
        return error(403, msg)
    elif isinstance(exc, exceptions.APIException):
        set_rollback()
        return error(exc.status_code, exc.detail)

    request = context.get('request')

    logger.error('Internal Server Error: %s', request.path,
                 exc_info=sys.exc_info(),
                 extra={
                     'status_code': 500,
                     'request': request
                 }
                 )
    return error(500, exc.message)

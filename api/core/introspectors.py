# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
import rest_framework_swagger.introspectors
from .utils import token_required_attr

try:
    import django_filters
except ImportError:
    django_filters = None


def form_param_to_query_param(params):
    for param in params:
        param['paramType'] = 'query'

    return params


class APIViewMethodIntrospector(rest_framework_swagger.introspectors.BaseMethodIntrospector):
    def get_docs(self):
        """
        Attempts to retrieve method specific docs for an
        endpoint. If none are available, the class docstring
        will be used
        """
        return self.retrieve_docstring()

    def build_query_parameters(self):
        params = super(APIViewMethodIntrospector, self).build_query_parameters()
        request_serializer = self.get_yaml_parser().object.get('request_serializer')

        if request_serializer is not None and not params:
            if self.get_http_method() in ['GET', 'HEAD', 'DELETE']:
                params = form_param_to_query_param(self.build_form_parameters())

        token_required = token_required_attr(self.callback, self.method)

        if token_required in ['required', 'optional']:
            params.insert(0, {
                'paramType': 'query',
                'name': 'token',
                'description': u'api token',
                'required': token_required == 'required',
                'type': 'string'})
        return params


class WrappedAPIViewMethodIntrospector(rest_framework_swagger.introspectors.BaseMethodIntrospector):
    def get_docs(self):
        """
        Attempts to retrieve method specific docs for an
        endpoint. If none are available, the class docstring
        will be used
        """
        return rest_framework_swagger.introspectors.get_view_description(self.callback)

    def get_module(self):
        from rest_framework_swagger.decorators import wrapper_to_func
        func = wrapper_to_func(self.callback)
        return func.__module__

    def get_notes(self):
        return self.parent.get_notes()

    def get_yaml_parser(self):
        parser = rest_framework_swagger.introspectors.YAMLDocstringParser(self)
        return parser

    def build_query_parameters(self):
        params = super(WrappedAPIViewMethodIntrospector, self).build_query_parameters()
        request_serializer = self.get_yaml_parser().object.get('request_serializer')

        if request_serializer is not None and not params:
            if self.get_http_method() in ['GET', 'HEAD', 'DELETE']:
                params = form_param_to_query_param(self.build_form_parameters())

        func, args, kwargs = resolve(self.path)

        token_required = getattr(func, 'token_required', '')
        if token_required in ['required', 'optional']:
            params.insert(0, {
                'paramType': 'query',
                'name': 'token',
                'description': u'api token',
                'required': token_required == 'required',
                'type': 'string'})
        return params

# -*- coding: utf-8 -*-
from api.views import login
from django.conf.urls import include, url
import common_urls

__author__ = 'ziven'

patterns = common_urls.urlpatterns + [
    url(r'^sms/$', login.SendSms.as_view(), name='api-sms'),
    url(r'^login/$', login.LoginView.as_view(), name='api-login'),
]

urlpatterns = [
    url(r'api/customer/', include(patterns))
]

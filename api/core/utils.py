# -*- coding: utf-8 -*-

import requests
from django.conf import settings

__author__ = 'ziven'


def token_required_attr(cls, method):
    """
    判断一个class view的某个方法是否需要token
    :param cls: view class
    :param method: GET, POST, ...
    :return:
    required
    optional
    ...
    """
    method = str(method).lower()
    if not hasattr(cls, method):
        return ''
    method = getattr(cls, method)
    # 优先取方法的装饰器, 方法没有则取类的
    return getattr(method, 'token_required', '') or getattr(cls, 'token_required', '')


def send_sms(mobile, content):
    """
    短信开通接口
    """
    url = ''
    params = {
        'method': 'Submit',
        'userCode': settings.SMS_ACCOUNT,
        'userPass': settings.SMS_PASSWORD,
        'DesNo': mobile,
        'Msg': content,
        'Channel': 0
    }
    r = requests.get(url, params=params)
    try:
        return ''
    except Exception, e:
        return '', e.message, ''

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

SMS_RET_DICT = {
    '-1': u'提交接口错误',
    '-3': u'用户名或密码错误',
    '-4': u'短信内容和备案的模板不一样',
    '-5': u'签名不正确（格式为：短信内容……【签名内容】）签名一定要放在短信最后',
    '-7': u'余额不足',
    '-8': u'通道错误',
    '-9': u'无效号码',
    '-10': u'签名内容不符合长度',
    '-11': u'用户有效期过期',
    '-12': u'黑名单',
    '-13': u'语音验证码的 Amount 参数必须是整形字符串',
    '-14': u'语音验证码的内容只能为数字',
    '-15': u'语音验证码的内容最长为 6 位',
    '-16': u'余额请求过于频繁，5 秒才能取余额一次',
    '-17': u'非法 IP',
    '-23': u'解密失败'
}


def send_sms(mobile, content):
    """
    触发通道已开通，开发文档下载：http://www.winnerlook.com/xzzx
    账号：KJKCF
    密码：KJKCF2015
    登录地址：http://cf.1069106.com
    http://121.199.48.186:1210/services/msgsend.asmx/SendMsg?userCode=string&userPass=string&DesNo=string&Msg=验证码:XXXX&Channel=0
    发送短信
    :param sms_log:
    :param sms_type:
    :return: code, msg, smsid
        code:   返回值为>0时，表示提交成功  错误代码 说明
                -1 提交接口错误
                -3 用户名或密码错误
                -4 短信内容和备案的模板不一样
                -5 签名不正确（格式为： 短信内容……【签名内容】）签名一定要放
                在短信最后
                -7 余额不足
                -8 通道错误
                -9 无效号码
                -10 签名内容不符合长度
                -11 用户有效期过期
                -12 黑名单
                -13 语音验证码的 Amount 参数必须是整形字符串
                -14 语音验证码的内容只能为数字
                -15 语音验证码的内容最长为 6 位
                -16 余额请求过于频繁，5 秒才能取余额一次
                -17 非法 IP
                -23 解密失败
        msg:    提交结果描述
        smsid:  仅当提交成功后，此字段值才有意义（消息ID）
    """
    url = 'http://121.199.48.186:1210/services/msgsend.asmx/SendMsg'
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
        result = r.text
        return result, SMS_RET_DICT[result] if result in SMS_RET_DICT else u'未知错误', result
    except Exception, e:
        return '', e.message, ''

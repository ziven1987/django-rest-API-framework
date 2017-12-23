# coding=utf-8
from api.core.exceptions import APIError
from api.core.models import SmsCode, Token
from apps.customer.models import Customer
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class SendSmsQuery(serializers.Serializer):
    mobile = serializers.RegexField(r'^1[3-9]\d{9}$', required=True, help_text=u'手机号')


class LoginQuerySerializer(serializers.Serializer):
    mobile = serializers.CharField(required=False, help_text=u'手机号')
    code = serializers.CharField(required=False, help_text=u'验证码')

    @staticmethod
    def _validate_user(user, attrs):
        if user is None:
            raise APIError(u'登录失败，请重试！')
        elif not user.is_active:
            raise APIError(u'此用户已被停用')
        attrs['user'] = user
        return attrs

    def validate(self, attrs):
        mobile = attrs.get('mobile')
        code = attrs.get('code')
        if mobile and code:
            sms = SmsCode.validate(mobile, code)
            if sms:
                customer, _ = Customer.objects.get_or_create(mobile=mobile)
                sms.mark_used()
                return self._validate_user(customer.user, attrs)
            else:
                raise APIError(u'验证码无效或者已经过期')

        return self._validate_user(None, attrs)


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ('token',)

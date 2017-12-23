# -*- coding: utf-8 -*-
import when
from datetime import timedelta
from api import serializers
from api.core.decorators import token_required
from api.core.exceptions import APIError
from api.core.models import Token, SmsCode
from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseLogin(APIView):
    @staticmethod
    def obtain_token(user):
        token, created = Token.objects.get_or_create(user=user)
        token.expire_time = when.future(months=1)
        token.save()
        return token

    @token_required
    def delete(self, request, format=None):
        """
        退出登录
        """
        request = request._request
        request.session.clear()
        request.session.delete()
        request.session = None
        return Response()


class LoginView(APIView):
    def post(self, request, format=None):
        """
        手机验证码换取token
        ---
        request_serializer: serializers.LoginQuerySerializer
        response_serializer: serializers.TokenSerializer
        """
        ser = serializers.LoginQuerySerializer(data=request.POST)
        if ser.is_valid():
            token = self.obtain_token(ser.validated_data['user'])
            ser = serializers.TokenSerializer(token)
            return Response(ser.data)

        return Response(ser.errors, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def obtain_token(user):
        token, created = Token.objects.get_or_create(user=user)
        token.expire_time = when.future(months=1)
        token.save()
        return token

    @token_required
    def delete(self, request, format=None):
        """
        退出登录
        """
        request = request._request
        request.session.clear()
        request.session.delete()
        request.session = None
        return Response()


class SendSms(APIView):

    def post(self, request):
        """
        发送短信验证码
        ---
        request_serializer: serializers.SendSmsQuery
        """
        ser = serializers.SendSmsQuery(data=request.data)
        ser.is_valid(True)
        mobile = ser.validated_data['mobile']
        try:
            last_send = SmsCode.objects.filter(mobile=mobile).latest('create_time').create_time
            if last_send + timedelta(seconds=30) > now():
                raise APIError(u'请求过于频繁!')
        except SmsCode.DoesNotExist:
            pass
        code = SmsCode.create(mobile)
        # 需要确定短信模板和短信接口
        # content = settings.LOGIN_SMS_TEMPLATE % code.code
        # send_sms(mobile, content)
        return Response(code.code)

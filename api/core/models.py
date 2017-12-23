# -*- coding: utf-8 -*-
import binascii
import random
from datetime import timedelta
import os
from django.db import models
from django.utils.timezone import now


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True, unique=True)
    user = models.OneToOneField('auth.User', related_name='auth_token')
    expire_time = models.DateTimeField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    @staticmethod
    def generate_key():
        return binascii.hexlify(os.urandom(20)).decode()

    @property
    def expired(self):
        if not self.expire_time:
            return False
        return self.expire_time < now()

    def __str__(self):
        return self.key


class SmsCode(models.Model):
    mobile = models.CharField(max_length=16, verbose_name=u'手机号码', db_index=True)
    code = models.CharField(max_length=16, verbose_name=u'验证码', db_index=True)
    used = models.BooleanField(default=False, verbose_name=u'是否已经使用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    expire_time = models.DateTimeField(null=True, verbose_name=u'过期时间')
    used_time = models.DateTimeField(null=True, verbose_name=u'使用时间')

    @property
    def expired(self):
        if not self.expire_time:
            return False
        return self.expire_time < now()

    @classmethod
    def create(cls, mobile, validity=60 * 5):
        seq = '0123456789'
        if mobile == '13800000000':  # AppStore审核使用
            code = '0000'
        else:
            code = ''.join([random.choice(seq) for i in range(4)])

        inst, _ = cls.objects.get_or_create(mobile=mobile, used=False)
        inst.code = code
        inst.create_time = now()
        inst.expire_time = inst.create_time + timedelta(seconds=validity)
        inst.save()
        return inst

    def mark_used(self):
        self.used = True
        self.used_time = now()
        self.save()

    @classmethod
    def validate(cls, mobile, code):
        try:
            sms = cls.objects.get(mobile=mobile, code=code, used=False)
            if sms.expired:
                return None
            return sms
        except cls.DoesNotExist:
            return None
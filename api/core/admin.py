from django.contrib import admin
from django.contrib.admin import register
from .models import *


@register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass


@register(SmsCode)
class SmsCodeAdmin(admin.ModelAdmin):
    pass

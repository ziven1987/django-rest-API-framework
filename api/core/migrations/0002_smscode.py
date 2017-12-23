# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=16, verbose_name='\u624b\u673a\u53f7\u7801', db_index=True)),
                ('code', models.CharField(max_length=16, verbose_name='\u9a8c\u8bc1\u7801', db_index=True)),
                ('used', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u7ecf\u4f7f\u7528')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('expire_time', models.DateTimeField(null=True, verbose_name='\u8fc7\u671f\u65f6\u95f4')),
                ('used_time', models.DateTimeField(null=True, verbose_name='\u4f7f\u7528\u65f6\u95f4')),
            ],
        ),
    ]

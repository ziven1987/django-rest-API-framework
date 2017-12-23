# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=40, unique=True, serialize=False, primary_key=True)),
                ('expire_time', models.DateTimeField(null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(related_name='auth_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

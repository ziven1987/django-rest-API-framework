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
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('mobile', models.CharField(unique=True, max_length=20, verbose_name='\u624b\u673a', db_index=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'app\u7528\u6237',
                'verbose_name_plural': 'app\u7528\u6237',
            },
        ),
    ]

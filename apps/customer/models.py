# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField('auth.User', related_name='customer')
    name = models.CharField(u'姓名', max_length=20)
    mobile = models.CharField(u'手机', max_length=20, db_index=True, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            user, _ = User.objects.get_or_create(username=self.mobile)
            self.user = user
        return super(Customer, self).save(*args, **kwargs)

    def delete(self, using=None):
        if self.user:
            self.user.delete()
        super(Customer, self).delete(using)

    def __unicode__(self):
        return u'[%d]-%s-%s' % (self.id, self.name, self.mobile)

    class Meta:
        verbose_name_plural = verbose_name = u'app用户'

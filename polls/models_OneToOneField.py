#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :models_OneToOneField.py
@说明        :模型一对一
@时间        :2020/04/14 13:50:07
@作者        :张强
@版本        :1.0
'''


from django.db import models

#3.一对一OneToOneField

from django.conf import settings

# 两个字段都使用一对一关联到了Django内置的auth模块中的User模型
class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )

# 跨模块的模型
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )    
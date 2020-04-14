#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :models_ManyToManyField.py
@说明        :多对多关系
@时间        :2020/04/14 13:47:47
@作者        :张强
@版本        :1.0
'''


from django.db import models

#2.多对多 ManyToManyField

# 参数说明：
# related_name
# 参考外键的相同参数。

# related_query_name
# 参考外键的相同参数。

# limit_choices_to
# 参考外键的相同参数。但是对于使用through参数自定义中间表的多对多字段无效。

# through 定义中间表
# through_fields
class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',       # 自定义中间表
        through_fields=('group', 'person'), 
    )

class Membership(models.Model):  # 这就是具体的中间表模型
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

# db_table 中间表名，不指定则默认


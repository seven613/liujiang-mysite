#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :models_ForeignKey.py
@说明        :模型--外键
@时间        :2020/04/14 13:48:06
@作者        :张强
@版本        :1.0
'''


from django.db import models

# 1.多对一（ForeignKey）
# 外键要定义在‘多’的一方！
class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    # ...

class Manufacturer(models.Model):
    # ...
    pass

class Car2(models.Model):
    manufacturer = models.ForeignKey(
        'production.Manufacturer',      #另一个应用中 关键在这里！！
        on_delete=models.CASCADE,
    )

# on_delete：参数，不可省略。
# CASCADE：模拟SQL语言中的ON DELETE CASCADE约束，将定义有外键的模型对象同时删除！（该操作为当前Django版本的默认操作！）
# PROTECT:阻止上面的删除操作，但是弹出ProtectedError异常
# SET_NULL：将外键字段设为null，只有当字段设置了null=True时，方可使用该值。
# SET_DEFAULT:将外键字段设为默认值。只有当字段设置了default参数时，方可使用。
# DO_NOTHING：什么也不做。
# SET()：设置为一个传递给SET()的值或者一个回调函数的返回值。注意大小写。

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )

# limit_choices_to 用于限制外键所能关联的对象，
staff_member = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True}, # 虽然是用User表的数据，但是不允许关联到User表
)
# related_name 关联对象反向引用模型的名称，系统默认modelname_set，modelname模型名小写；related_name可以更改名字
class Car3(models.Model):
    manufacturer = models.ForeignKey(
        'production.Manufacturer',      
        on_delete=models.CASCADE,
        related_name='car_producted_by_this_manufacturer',  # 反向引用默认应为Manufacturer_set,但是这里给改名字了
    )
# related_query_name 反向关联查询名,用于从目标模型反向过滤模型对象的名称
class Tag(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",       # 注意这一行
    )
    name = models.CharField(max_length=255)

# 现在可以使用‘tag’作为查询名了
Article.objects.filter(tag__name="important")

# to_field 外键关联默认都关联到主键上，一般是id.这个参数可以指定到其他字段上，但是这个字段unique=True
# db_constraint默认为True,遵循数据库约束

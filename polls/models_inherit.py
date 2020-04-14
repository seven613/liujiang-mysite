#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :models_inherit.py
@说明        :模型继承
@时间        :2020/04/14 14:31:13
@作者        :张强
@版本        :1.0
'''
from django.db import models
'''
        1.抽象基类
    方法：Meta中abstract=True
    不会生成表，只能作为其他类继承使用
'''

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True #设置为抽象基类


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):#继承父类的元素属性
        dd_table ='student_info'



#2.

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :models_meta.py
@说明        :模型的元素数据Meta
@时间        :2020/04/14 13:47:25
@作者        :张强
@版本        
'''
from django.db import models


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta: #模型的子类,每个模型都可以有这个子类，这个子类只对自己的父类起作用
        abstract=True # 认为父类是一个抽象模型，不生成数据库表，只能被其他模型继承
        app_label ='myapp' # 模型的app没有在INSTALLED_APPS中注册，则必须声明模型属于哪个app
        base_manager_name ='_ox_base_manager'# 定义模型的_base_manager管理器的名字。模型管理器是django提供的API
        db_table ='my_friends' #在数据库中生成的表名字
        db_tablespace ='' #数据库表空间的名字，默认值是 DEFAULT_TABLESPACE设置
        default_manager_name ='_ox_default_manager'#自定义_default_manager管理器的名字
        default_related_name ='ox_set'#从一个模型反向关联设置有关系字段的源模型，默认model_name_set
        get_latest_by ="order_date"#指定一个类似 DateField、DateTimeField或者IntegerField这种可以排序的字段，作为latest()和earliest()方法的排序依据，从而得出最近一个或最前面一个对象
        managed =True  #按照既定规则，管理数据库表的生命周期。设置未false 将不创建数据库表
        order_with_respect_to='horn_length' #根据指定字段排序，用get_modelname_order和set_moldername_order获取顺序后设置顺序
        ordering=['-pub_date','author'] #表示按pub_date降序,author升序 排序
        permissions=(('can_deliver_pizzas','可以送披萨'))#创建对象时增加额外的权限。
        default_permissions=('add','change','delete') #模型的默认权限就是增删改，可以自定义设置
        proxy=True #使用代理模式的模型继承方式
        required_db_features=['gis_enabled'] #声明模型依赖的数据功能。模型建立依赖GIS功能
        required_db_vendor='sqlite'#声明模型支持的数据库,django模型默认支持sqlite,mysql,postgresql,oracle
        select_on_save = True#使用django.db.models.Model.save()算法保存对象，默认是False
        indexes =  [ #接收一个应用在当前模型上的索引列表
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]
        unique_together=(('name', 'birth_day', 'address'),)#数据库的联合约束
        index_together #废弃
        verbose_name='披萨'#最常用，设置对象直观、可读的名称。apple
        verbose_name_plural =verbose_name #复数形式 ,apples
        label #等同于app_label.object_name,只读
        label_lower #小写模型名



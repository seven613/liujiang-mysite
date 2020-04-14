#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :models_ex.py
@说明        :模型的字段类型
@时间        :2020/04/14 13:48:39
@作者        :张强
@版本        :1.0
'''



 from django.db import models
# 类型	说明
# AutoField	一个自动增加的整数类型字段。通常你不需要自己编写它，Django会自动帮你添加字段：id = models.AutoField(primary_key=True)，这是一个自增字段，从1开始计数。如果你非要自己设置主键，那么请务必将字段设置为primary_key=True。Django在一个模型中只允许有一个自增字段，并且该字段必须为主键！
# BigAutoField	(1.10新增)64位整数类型自增字段，数字范围更大，从1到9223372036854775807
# BigIntegerField	64位整数字段（看清楚，非自增），类似IntegerField ，-9223372036854775808 到9223372036854775807。在Django的模板表单里体现为一个textinput标签。
# BinaryField	二进制数据类型。使用受限，少用。
# BooleanField	布尔值类型。默认值是None。在HTML表单中体现为CheckboxInput标签。如果要接收null值，请使用NullBooleanField。
# CharField	字符串类型。必须接收一个max_length参数，表示字符串长度不能超过该值。默认的表单标签是input text。最常用的filed，没有之一！
# CommaSeparatedIntegerField	逗号分隔的整数类型。必须接收一个max_length参数。常用于表示较大的金额数目，例如1,000,000元。
# DateField	class DateField(auto_now=False, auto_now_add=False, **options)日期类型。一个Python中的datetime.date的实例。在HTML中表现为TextInput标签。在admin后台中，Django会帮你自动添加一个JS的日历表和一个“Today”快捷方式，以及附加的日期合法性验证。两个重要参数：（参数互斥，不能共存） auto_now:每当对象被保存时将字段设为当前日期，常用于保存最后修改时间。auto_now_add：每当对象被创建时，设为当前日期，常用于保存创建日期(注意，它是不可修改的)。设置上面两个参数就相当于给field添加了editable=False和blank=True属性。如果想具有修改属性，请用default参数。例子：pub_time = models.DateField(auto_now_add=True)，自动添加发布时间。
# DateTimeField	日期时间类型。Python的datetime.datetime的实例。与DateField相比就是多了小时、分和秒的显示，其它功能、参数、用法、默认值等等都一样。
# DecimalField	固定精度的十进制小数。相当于Python的Decimal实例，必须提供两个指定的参数！参数max_digits：最大的位数，必须大于或等于小数点位数 。decimal_places：小数点位数，精度。 当localize=False时，它在HTML表现为NumberInput标签，否则是text类型。例子：储存最大不超过999，带有2位小数位精度的数，定义如下：models.DecimalField(..., max_digits=5, decimal_places=2)。
# DurationField	持续时间类型。存储一定期间的时间长度。类似Python中的timedelta。在不同的数据库实现中有不同的表示方法。常用于进行时间之间的加减运算。但是小心了，这里有坑，PostgreSQL等数据库之间有兼容性问题！
# EmailField	邮箱类型，默认max_length最大长度254位。使用这个字段的好处是，可以使用DJango内置的EmailValidator进行邮箱地址合法性验证。
# FileField	class FileField(upload_to=None, max_length=100, **options)上传文件类型，后面单独介绍。
# FilePathField	文件路径类型，后面单独介绍
# FloatField	浮点数类型，参考整数类型
# ImageField	图像类型，后面单独介绍。
# IntegerField	整数类型，最常用的字段之一。取值范围-2147483648到2147483647。在HTML中表现为NumberInput标签。
# GenericIPAddressField	class GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)[source],IPV4或者IPV6地址，字符串形式，例如192.0.2.30或者2a02:42fe::4在HTML中表现为TextInput标签。参数protocol默认值为‘both’，可选‘IPv4’或者‘IPv6’，表示你的IP地址类型。
# NullBooleanField	类似布尔字段，只不过额外允许NULL作为选项之一。
# PositiveIntegerField	正整数字段，包含0,最大2147483647。
# PositiveSmallIntegerField	较小的正整数字段，从0到32767。
# SlugField	slug是一个新闻行业的术语。一个slug就是一个某种东西的简短标签，包含字母、数字、下划线或者连接线，通常用于URLs中。可以设置max_length参数，默认为50。
# SmallIntegerField	小整数，包含-32768到32767。
# TextField	大量文本内容，在HTML中表现为Textarea标签，最常用的字段类型之一！如果你为它设置一个max_length参数，那么在前端页面中会受到输入字符数量限制，然而在模型和数据库层面却不受影响。只有CharField才能同时作用于两者。
# TimeField	时间字段，Python中datetime.time的实例。接收同DateField一样的参数，只作用于小时、分和秒。
# URLField	一个用于保存URL地址的字符串类型，默认最大长度200。
# UUIDField	用于保存通用唯一识别码（Universally Unique Identifier）的字段。使用Python的UUID类。在PostgreSQL数据库中保存为uuid类型，其它数据库中为char(32)。这个字段是自增主键的最佳替代品，后面有例子展示。

#FileField 文件类型
class MyModel(models.Model):
    # 文件被传至`MEDIA_ROOT/uploads`目录，MEDIA_ROOT由你在settings文件中设置
    upload = models.FileField(upload_to='uploads/')
    # 或者
    # 被传到`MEDIA_ROOT/uploads/2015/01/30`目录，增加了一个时间划分
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')


 def user_directory_path(instance, filename):
    #文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel1(models.Model):
    upload = models.FileField(upload_to=user_directory_path)   #upload_to 使用的是回调函数

# ImageField 图片类型
# 必须安装pillow包
# 使用步骤：
# 1.在settings文件中，配置MEDIA_ROOT，作为你上传文件在服务器中的基本路径（为了性能考虑，这些文件不会被储存在数据库中）。再配置个MEDIA_URL，作为公用URL，指向上传文件的基本路径。请确保Web服务器的用户账号对该目录具有写的权限。
# 2.添加FileField或者ImageField字段到你的模型中，定义好upload_to参数，文件最终会放在MEDIA_ROOT目录的“upload_to”子目录中。
# 3.所有真正被保存在数据库中的，只是指向你上传文件路径的字符串而已。可以通过url属性，在Django的模板中方便的访问这些文件。例如，假设你有一个ImageField字段，名叫mug_shot，那么在Django模板的HTML文件中，可以使用{{ object.mug_shot.url }}来获取该文件。其中的object用你具体的对象名称代替。
# 4.可以通过name和size属性，获取文件的名称和大小信息。


# FilePathField 文件路径类型
# 字符串形式，最大长度100，
path：必须指定的参数。表示一个系统绝对路径。

match:可选参数，一个正则表达式，用于过滤文件名。只匹配基本文件名，不匹配路径。例如foo.*\.txt$，只匹配文件名foo23.txt，不匹配bar.txt与foo23.png。

recursive:可选参数，只能是True或者False。默认为False。决定是否包含子目录，也就是是否递归的意思。

allow_files:可选参数，只能是True或者False。默认为True。决定是否应该将文件名包括在内。它和allow_folders其中，必须有一个为True。

allow_folders： 可选参数，只能是True或者False。默认为False。决定是否应该将目录名包括在内。
# UUIDField 
import uuid     # Python的内置模块
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 其它字段
from django.db import models

# null 该值为True时，Django在数据库用NULL保存空值。默认值为False。对于保存字符串类型数据的字段，请尽量避免将此参数设为True，那样会导致两种‘没有数据’的情况，一种是NULL，另一种是‘空字符串’。
#blank True时，字段可以为空。默认False。和null参数不同的是，null是纯数据库层面的，而blank是验证相关的，它与表单验证是否允许输入框内为空有关，与数据库无关。所以要小心一个null为False，blank为True的字段接收到一个空值可能会出bug或异常。
#choices 用于页面上的选择框标签，需要先提供一个二维的二元元组，第一个元素表示存在数据库内真实的值，第二个表示页面上显示的具体内容。在浏览器页面上将显示第二个元素的值。例如
class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

class Person(models.Model):
    SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
# >>> p = Person(name="Fred Flintstone", shirt_size="L")
# >>> p.save()
# >>> p.shirt_size
# 'L'
# >>> p.get_shirt_size_display() 获取choices的第二元素值
# 'Large'


# db_column该参数用于定义当前字段在数据表内的列名。如果未指定，Django将使用字段名作为列名。

# db_index该参数接收布尔值。如果为True，数据库将为该字段创建索引。

# db_tablespace用于字段索引的数据库表空间的名字，前提是当前字段设置了索引。默认值为工程的DEFAULT_INDEX_TABLESPACE设置。如果使用的数据库不支持表空间，该参数会被忽略。
# default字段的默认值，可以是值或者一个可调用对象。如果是可调用对象，那么每次创建新对象时都会调用。设置的默认值不能是一个可变对象，比如列表、集合等等。lambda匿名函数也不可用于default的调用对象，因为匿名函数不能被migrations序列化。
# editable# 如果设为False，那么当前字段将不会在admin后台或者其它的ModelForm表单中显示，同时还会被模型验证功能跳过。参数默认值为True。

# error_messages# 用于自定义错误信息。参数接收字典类型的值。字典的键可以是null、 blank、 invalid、 invalid_choice、 unique和unique_for_date其中的一个。

# help_text# 额外显示在表单部件上的帮助文本。使用时请注意转义为纯文本，防止脚本攻击。

# primary_key
# 如果你没有给模型的任何字段设置这个参数为True，Django将自动创建一个AutoField自增字段，名为‘id’，并设置为主键。也就是id = models.AutoField(primary_key=True)。
# 如果你为某个字段设置了primary_key=True，则当前字段变为主键，并关闭Django自动生成id主键的功能。
# primary_key=True隐含null=False和unique=True的意思。一个模型中只能有一个主键字段！

# unique
# 设为True时，在整个数据表内该字段的数据不可重复

# unique_for_date
# 日期唯一。可能不太好理解。举个栗子，如果你有一个名叫title的字段，并设置了参数unique_for_date="pub_date"，那么Django将不允许有两个模型对象具备同样的title和pub_date。有点类似联合约束。

# unique_for_month
# 同上，只是月份唯一。

# unique_for_year
# 同上，只是年份唯一。

# verbose_name
# 为字段设置一个人类可读，更加直观的别名

# validators
# 运行在该字段上的验证器的列表。
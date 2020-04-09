from django.contrib import admin

from .models import Question,Choice

admin.site.register(Question)# 注册模型，后台管理就可以看见了
admin.site.register(Choice)
from django.contrib import admin

from .models import Question,Choice


class ChoiceLine(admin.TabularInline): # 前端显示选择项的方式 TabularInline 横向显示  ；StackedInline 纵向显示
    model = Choice
    extra = 3 #前端显示选择项的数量

class QuestionAdmin(admin.ModelAdmin):
    # fields =['pub_date','question_text'] # 可以改变顺序，前端页面显示顺序也会改变
    fieldsets=[
        (None,  {'fields': ['question_text']}),
        ('Date Information',  {'fields': ['pub_date']}),
    ]
    inlines =[ChoiceLine] #控制关联选择项的多少 和显示方向 横向、纵向

    list_display =('question_text','pub_date','was_published_recently') #前端显示的列

    list_filter = ['pub_date'] #使用过滤，前端增加过滤组件

    search_fields = ['question_text'] #增加搜索框，注意：搜索都是SQL 中的Like ，效率不高

admin.site.register(Question,QuestionAdmin)# 注册模型，后台管理就可以看见了
admin.site.register(Choice)
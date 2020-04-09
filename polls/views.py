from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render


from .models import Question

def index(request):
    # return HttpResponse("主页") # 占位用
    latest_question_list = Question.objects.order_by('pub_date')[:5] # 取最近5个问题
    # output =','.join([q.question_text for q in latest_question_list]) # 列表推导式，将5个问题的内容用逗号连起来
    # return HttpResponse(output)
    content ={
        'latest_question_list':latest_question_list
    }
    """使用模版
    template = loader.get_template('polls/index.html') #使用模版
    return HttpResponse(template.render(content,request))
    """

    """
    使用render快捷键
    """
    return render(request,'polls/index.html',content)

    
def detail(request,question_id):
    return HttpResponse("问题:%s 页面" % question_id)

def results(request,question_id):
    return HttpResponse("问题:%s的投票结果页" % question_id)

def vote(request,question_id):
    return HttpResponse("问题：%s 的投票数" % question_id)
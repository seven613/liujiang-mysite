from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader

from django.shortcuts import render,get_object_or_404


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
    # return HttpResponse("问题:%s 页面" % question_id)
    """
    1.查找问题，不存在就抛异常
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("不存在的问题") # 抛出异常
    """
    """
    2.使用快捷键get_object_or_404
    """
    question = get_object_or_404(Question,pk=question_id)

    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    # return HttpResponse("问题:%s的投票结果页" % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    # return HttpResponse("问题：%s 的投票数" % question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':'没有选择'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
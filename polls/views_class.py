from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question,Choice

#一般情况下，使用ListView,DetailView如下示例即可。
#template_name 会自动默认，然后根据模版视图，自动生成上下文变量'question_list'，不需要另行指定context_object_name
class ExIndexView(generic.ListView):
    model = Question

class ExDetailView(generic.DetailView):
    model = Question



# ListView 默认template_name = 'polls/Question_list.html',即'app/model_list.html',也可以如下自己指定
class IndexView(generic.ListView):
    #此处并未指定模型，使用的是上下文变量context_object_name代替了model
    template_name='polls/index.html'
    context_object_name='latest_question_list' #上下文变量，代替了model

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# DetailView 需要捕获url中的关键字pk,所以视图中改为<int:pk>
# DetailView 默认template_name = 'polls/Question_detail.html',即'app/model_detail.html',也可以如下自己指定
class DetailView(generic.DetailView):
    model=Question # 使用类视图必须指定模型
    template_name='polls/detail.html'

class ResultView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

def vote(request,question_id):
    # return HttpResponse("问题：%s 的投票数" % question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':'没有选择'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
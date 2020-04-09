from django.http import HttpResponse


def index(request):
    return HttpResponse("主页")

    
def detail(request,question_id):
    return HttpResponse("问题:%s 页面" % question_id)

def results(request,question_id):
    return HttpResponse("问题:%s的投票结果页" % question_id)

def vote(request,question_id):
    return HttpResponse("问题：%s 的投票数" % question_id)
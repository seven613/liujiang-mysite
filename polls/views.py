from django.http import HttpResponse


def index(request):
    return HttpResponse("主页")

    
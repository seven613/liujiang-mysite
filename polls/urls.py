from django.urls import path

from . import views
from . import views_class


app_name='polls' #命名空间

urlpatterns =  [
    
    # 原始模式，代码多，不易复用
    # path('',views.index,name='index'),
    # path('<int:question_id>/',views.detail,name='detail'),
    # path('<int:question_id>/results/',views.results,name='results'),
    # path('<int:question_id>/vote/',views.vote,name='vote'),
    
    # 使用类视图
    
    path('',views_class.IndexView.as_view(),name='index'),
    path('<int:pk>/',views_class.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views_class.ResultView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
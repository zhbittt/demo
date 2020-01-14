from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('index', views.index),
    path('wechat', views.wechat),
    path('gettoken', views.gettoken),
    path('getapprovaldetail', views.getapprovaldetail),
    path('applyevent', views.applyevent),
    path('applyeventcallback', views.applyeventcallback),
]

# coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r"^blog/$", views.blog, name='blog'),
    url(r"^tool/$", views.tool, name="tool"),
    url(r"^aboutme/$",views.aboutme,name="aboutme"),
    url(r"^blog/(\d+)$",views.post,name="post"),
    url(r"^editpost/(\d+|\w+)$",views.editpost,name='editpost'),
    url(r"^769007157/$",views.login,name="login"),
    url(r"^logout/$",views.logout,name="logout"),
    url(r"^register",views.register,name="register"),
    url(r"^delpost/(\d+)",views.delpost,name="delpost"),
    url(r"^xss-test",views.xss,name="xss"),
]

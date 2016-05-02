# coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r"^blog/$", views.blog, name='blog'),
    url(r"^tool/$", views.tool, name="tool"),
    url(r"^aboutme/$",views.aboutme,name="aboutme"),
    url(r"^blog/(\d)$",views.post,name="post"),
    url(r"^editpost/(\d)$",views.editpost,name='editpost'),
    # url(r"^delect/(\d)$",views.delectpost,name="delectpost")
    url(r"^769007157/$",views.login,name="login")
]

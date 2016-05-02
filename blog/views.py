# -*- coding: utf-8
from django.http import HttpResponse


def sum(request,num):
    html="""<h1>您输入的是%s</h1> """ %num
    return HttpResponse(html)
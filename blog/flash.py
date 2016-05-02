# -*- coding: utf-8

def add(request,msg,msgtype):
    request.session["msg"]=msg
    request.session["msgtype"]=msgtype


def success(request,msg):
    add(request,msg,msgtype="success")

def info(request,msg):
    add(request,msg,msgtype="info")

def warning(request,msg):
    add(request,msg,msgtype="warning")

def error(request,msg):
    add(request,msg,msgtype="error")

def clear(request,msg):
    add(request,msg,msgtype="clear")



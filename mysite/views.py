from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Blog
from django.shortcuts import render_to_response
from mysite.form import EditPostForm
from django.contrib import auth #用户验证
from django.template.context import RequestContext
from mysite.form import LoginForm
from blog import flash
# Create your views here.

#
# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     type = models.IntegerField(default=0)
#     img = models.CharField(max_length=500, null=True) # 博客导图
#     summary = models.CharField(max_length=500, null=True)
#     rss = models.CharField(max_length=1024, null=True)  # 订阅源
#     content = models.TextField()
#     content_show =models.TextField(u'正文显示', null=True)
#     add_date = models.DateTimeField()
#     counts = models.IntegerField(default=0)     # 点击率
#     is_show = models.CharField(max_length=100, null=True)        # 加密




def index(requests):

    # return HttpResponse("test")
    return render_to_response("index.html")


def blog(request):
    content=Blog.objects.order_by("add_date")
    # print(body)
    # body="bjkhgjkhjkhjk"
    return render_to_response("blog.html",{"content":content})



def tool(request):

    return render(request,template_name="tool.html")



def aboutme(request):

    return render(request,template_name="aboutme.html")




def post(request,pid):
    post=Blog.objects.get(id=pid)
    return render_to_response("post.html",{"post":post})


def editpost(request,pid):
    post=Blog.objects.get(id=pid)
    return render_to_response("editpost.html",{"post":post,"EditPostForm":EditPostForm})


def login(request):
    print("fsd")
    if request.method=="GET":
        return render_to_response("login.html",dict(form=LoginForm),context_instance=RequestContext(request))
    else:
        form=LoginForm()
        email=request.POST.get("email","")
        password=request.POST.get("password","")

        user=auth.authenticate(user=email,password=password)
        print(user)
        if user is not None and user.is_active:
            print(u"登陆成功")
            auth.login(request,user)
            # request.user.message_set.create(message=u"正在处理中，请等待五分钟后刷新此页面...")
            return render_to_response("index.html",context_instance=RequestContext(request))
        else:
            # request.user.message_set.create(message=u"正在处理中，请等待五分钟后刷新此页面...")
            print("fail")
            flash.warning(request,u"用户名或密码错误")
            return render_to_response("login.html",{"form":LoginForm},context_instance=RequestContext(request))


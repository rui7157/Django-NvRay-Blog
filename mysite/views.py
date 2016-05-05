from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Blog
from django.shortcuts import render_to_response,redirect
from django.contrib import auth #用户验证
from django.template.context import RequestContext
from mysite.form import LoginForm,EditPostForm
from django.views.decorators.http import require_GET
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

#
# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     type = models.IntegerField(default=0)
#     img = models.CharField(max_lengt h=500, null=True) # 博客导图
#     summary = models.CharField(max_length=500, null=True)
#     rss = models.CharField(max_length=1024, null=True)  # 订阅源
#     content = models.TextField()
#     content_show =models.TextField(u'正文显示', null=True)
#     add_date = models.DateTimeField()
#     counts = models.IntegerField(default=0)     # 点击率
#     is_show = models.CharField(max_length=100, null=True)        # 加密




def index(request):

    return render_to_response("index.html",context_instance=RequestContext(request))


def blog(request):
    content=Blog.objects.order_by("add_date")
    return render_to_response("blog.html",{"content":content},context_instance=RequestContext(request))



def tool(request):

    return render(request,template_name="tool.html")



def aboutme(request):

    return render(request,template_name="aboutme.html")




def post(request,pid):
    post=Blog.objects.get(id=pid)
    return render_to_response("post.html",{"post":post},context_instance=RequestContext(request))

@login_required
def editpost(request,pid):
    if request.method=="GET":
        print("pid:",pid)
        if pid!="new":
            post=Blog.objects.get(id=pid)
        else:
            post=None
        return render_to_response("editpost.html",{"post":post,"form":EditPostForm},context_instance=RequestContext(request))
    else:
        pid=request.POST.get("id","new")
        title=request.POST.get("title","")
        content=request.POST.get("content","")
        print(pid=="new")
        if title!="" and content!="":
            # try:

            if pid=="new":
                post=Blog(title=title,content=content)
            else:
                post=Blog.objects.get(id=int(pid))
                post.title=title
                post.content=content
            post.save()
            messages.success(request,u"发帖成功！")
            return redirect(reverse('mysite.views.post', args=[pid,]))
            # except Exception:
            #     messages.warning(request,u"发帖失败！")
        else:
            messages.warning(request,u"标题或内容为空")
        print("失败pid：",pid)
        return redirect(reverse('mysite.views.editpost', args=[pid,]))

@require_GET
@login_required
def delpost(request,pid):
    post=Blog.objects.get(id=pid)
    messages.success(request,"删除成功")
    return redirect(reverse("blog"))



def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            newuser=form.save()
            print(newuser)
            auth.login(newuser)
            messages.success(u"注册成功")
            return redirect(reverse("mysite.views.index"))

        else:
            return render_to_response("register.html",{"form":form},context_instance=RequestContext(request))
    else:
        form=UserCreationForm()
        return render_to_response("register.html",{"form":form},context_instance=RequestContext(request))



def login(request):

    if request.method=="GET":
        return render_to_response("login.html",dict(form=LoginForm),context_instance=RequestContext(request))
    else:
        user_email=request.POST.get("email_name","")
        password=request.POST.get("password","")
        print("user:",user_email,"pws:",password)
        if "@" in user_email:
            print(u"email登陆")
            user=auth.authenticate(email=user_email,password=password)
        else:
            user=auth.authenticate(username=user_email,password=password)
        print(user)
        if user is not None and user.is_active:
            print(u"登陆成功")
            auth.login(request,user)
            # request.user.message_set.create(message=u"正在处理中，请等待五分钟后刷新此页面...")
            return render_to_response("index.html",context_instance=RequestContext(request))
        else:
            # request.user.message_set.create(message=u"正在处理中，请等待五分钟后刷新此页面...")
            print("fail")
            # flash.warning(request,u"用户名或密码错误")
            messages.warning(request,"用户名或者密码错误")
            return render_to_response("login.html",{"form":LoginForm},context_instance=RequestContext(request))


@login_required
def logout(request):
    auth.logout(request)
    messages.info(request,u"您已退出登陆")
    return redirect(reverse('mysite.views.index'))


def xss(request):
    cookie=request.GET.get("cookie")
    print(cookie)
    return render_to_response("tool.html",{"cookie":cookie})
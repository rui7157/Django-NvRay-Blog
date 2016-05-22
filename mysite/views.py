from django.shortcuts import render
from mysite.models import Blog, BlogTag, Tag
from django.shortcuts import render_to_response, redirect
from django.contrib import auth  # 用户验证
from django.template.context import RequestContext
from mysite.form import LoginForm, EditPostForm
from django.views.decorators.http import require_GET
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from random import randint


def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))


def blog(request, tagid):
    if tagid:
        tags = get_object_or_404(Tag,id=tagid)
        content = [blogtag.blog for blogtag in tags.blogtag_set.all()]
    else:
        content = Blog.objects.order_by("-add_date")
    tag=[(randint(1,5),name) for name in Tag.objects.all()]
    # tag = Tag.objects.all()  # 标签
    return render_to_response("blog.html", {"content": content, "tag": tag}, context_instance=RequestContext(request))


def tool(request):
    return render(request, template_name="tool.html")


def aboutme(request):
    return render(request, template_name="aboutme.html")


def post(request, pid):
    post = get_object_or_404(Blog,id=pid)
    post.counts+=1
    post.save()
    return render_to_response("post.html", {"post": post}, context_instance=RequestContext(request))


@login_required
def editpost(request, pid):
    def saveblogsave(tag):
        for tagname in tag:
            alltagname = [name.name for name in Tag.objects.all()]
            if tagname in alltagname:
                BlogTag(blog=blog, tag=Tag.objects.get(name=tagname)).save()
            else:
                if tagname:
                    print(u"存在",tagname)
                    tagobj = Tag(name=tagname)
                    tagobj.save()
                    BlogTag(blog=blog, tag=tagobj).save()


    if request.method == "GET":
        if pid != "new":
            post = Blog.objects.get(id=pid)
        else:
            post = None
        return render_to_response("editpost.html", {"post": post, "form": EditPostForm},
                                  context_instance=RequestContext(request))
    else:
        pid = request.POST.get("id", "new")
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        tag = request.POST.get("tag", "").split("|")
        if title != "" and content != "":
            # try:
                if pid == "new":
                    blog = Blog(title=title, content=content)
                    blog.save()
                    saveblogsave(tag)
                else:
                    blog = Blog.objects.get(id=int(pid))
                    blog.title = title
                    blog.content = content
                    blog.save()
                    saveblogsave(tag)

                messages.success(request, u"发帖成功！")
                return redirect(reverse('mysite.views.blog'))
            # except Exception:
            #     messages.warning(request, u"发帖失败！")
        else:
            messages.warning(request, u"标题或内容为空")
        print("失败pid：", pid)
        return redirect(reverse('mysite.views.editpost', args=[pid, ]))


@require_GET
@login_required
def delpost(request, pid):
    Blog.objects.get(id=pid).delete()
    messages.success(request, "删除成功")
    return redirect(reverse("blog"))


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            # auth.login(newuser)
            messages.success(u"注册成功")
            return redirect(reverse("mysite.views.index"))
        else:
            return render_to_response("register.html", {"form": form}, context_instance=RequestContext(request))
    else:
        form = UserCreationForm()
        return render_to_response("register.html", {"form": form}, context_instance=RequestContext(request))


def login(request):
    if request.method == "GET":
        return render_to_response("login.html", dict(form=LoginForm), context_instance=RequestContext(request))
    else:
        user_email = request.POST.get("email_name", "")
        password = request.POST.get("password", "")
        if "@" in user_email:
            user = auth.authenticate(email=user_email, password=password)
        else:
            user = auth.authenticate(username=user_email, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return render_to_response("index.html", context_instance=RequestContext(request))
        else:
            messages.warning(request, "用户名或者密码错误")
            return render_to_response("login.html", {"form": LoginForm}, context_instance=RequestContext(request))


@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, u"您已退出登陆")
    return redirect(reverse('mysite.views.index'))


def xss(request):
    cookie = request.GET.get("cookie")
    return render_to_response("tool.html", {"cookie": cookie})

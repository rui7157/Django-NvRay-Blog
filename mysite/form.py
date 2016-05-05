# -*- coding: utf-8
# from django.forms import Form
from django.forms import *
class LoginForm(Form):
    email_name = CharField(label=u"账号",widget=TextInput(attrs={'placeholder':u"邮箱或用户名",}),required=False)  # ,"用户名格式错误"
    # username = CharField(label=u"用户",widget=TextInput(attrs={'placeholder':u"密码",}) ,min_length=6) # ,"密码格式错误"
    password = CharField(label=u"密码",widget=PasswordInput(attrs={'placeholder':u"密码",}) ,min_length=6) # ,"密码格式错误"
    remember_me=BooleanField(label=u"记住登陆状态")
    # submit = SubmitField(u"登陆")

class RegisterForm(Form):
    email = CharField(label=u"邮箱", required=False)
    username = CharField(label=u"用户名：", required=False, min_length=3,max_length=20)  # ,"用户名格式错误"
    password = CharField(label=u"密码：",widget=PasswordInput, required=False,min_length=6,max_length=16)#格式错误"
    password2 = CharField(label=u"再次输入密码：",widget=PasswordInput,required=False)  # ,"密码格式错误"
    # submit = SubmitField(u"注册")

class EditPostForm(Form):
    title=CharField(label=u"*标题", error_messages={'required': '请输入标题'},widget=TextInput(attrs={'placeholder':u"标题",}))
    # content=CharField(u"dff",validators=[Required(u"不能为空")])
    content=CharField(label=u"",error_messages={'required': '请输入内容'},widget=Textarea(attrs={"name":u"content","id":u"content","class":u"ckeditor"}))
    # submit = SubmitField(u"发表")
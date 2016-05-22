#coding=utf-8
from django.db import models
from django.utils.safestring import mark_safe
import markdown
import bleach
from time import localtime


class Type(models.Model):
    """分类"""
    name = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def getCount(self):
        """获取数目"""
        return Blog.objects.filter(type=self.id).count()

    class Meta:
        db_table = 'type'



class Blog(models.Model):
    # id = models.IntegerField(null=False,primary_key=True)
    title = models.CharField(max_length=100)
    type = models.IntegerField(default=0)
    img = models.CharField(max_length=500, null=True) # 博客导图
    summary = models.CharField(max_length=500, null=True)
    rss = models.CharField(max_length=1024, null=True)  # 订阅源
    content = models.TextField()
    content_show =models.TextField(u'正文显示', null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    counts = models.IntegerField(default=0)     # 点击率
    is_show = models.CharField(max_length=100, null=True)        # 加密
    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None):
        #过滤非法标签
        # allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
        # 'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul','img',
        # 'h1', 'h2', 'h3', 'p','blockquote','hr','s']
        #
        # a_attrs = ['href', 'rel', 'title']
        # img_attrs = ['align', 'alt', 'border', 'height','src', 'width']
        # basic_attrs = ['class', 'dir', 'lang', 'title']
        # attrs={
        # 'a': a_attrs,
        # 'img': img_attrs,
        #
        # 'abbr':    basic_attrs,
        # 'acronym': basic_attrs,
        # 'div': basic_attrs,
        # 'span': basic_attrs,
        # 'p': basic_attrs,
        # }
        # self.content_show=bleach.linkify(bleach.clean(self.content,tags=allowed_tags,attributes=attrs,strip=True))
        self.content_show=self.content
        super(Blog, self).save()

    class Meta:
        db_table = 'blog'

        
        
    def getType(self):
        """获取类型"""
        return Type.objects.get(pk=self.type)

    def getTags(self):
        """获取标签"""
        return BlogTag.objects.filter(blog=self.id)






class Tag(models.Model):
    """个人标签"""
    # id = models.IntegerField(null=False,primary_key=True)
    name = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'tags'



class BlogTag(models.Model):
    """主题标签"""
    id = models.IntegerField(null=False,primary_key=True)
    blog = models.ForeignKey(Blog)
    tag = models.ForeignKey(Tag)
    add_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.tag.name
    class Meta:
        db_table = 'blog_tag'



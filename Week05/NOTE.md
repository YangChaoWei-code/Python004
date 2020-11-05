学习笔记

为什么要阅读源码?

• 解决文档里没有描述的特定问题 
• 二次开发 
• 学习语言--代码风格、规范、高级语法 
• 学习设计模式--接口、框架、架构 
• 学习算法 
• 阅读源代码不是唯一的学习手段，也不是最高效的那个

Django简介

• Django是一个开放源代码的Web应用框架
• 最初用于管理劳伦斯出版集团旗下的一些以新闻内容为主的网站
• 2005年7月在BSD许可证下发布

MTV框架模式主要是指：
• 模型（Model） 
• 模板（Template） 
• 视图（Views

Django的特点：
• 采用了MTV的框架 
• 强调快速开发和代码复用DRY(Do Not Repeat Yourself) 
• 组件丰富： 
        ORM(对象关系映射) 
		映射类来构建数据模型 
		URL支持正则表达式 
		模板可继承 
		内置用户认证，提供用户认证和权限功能 
		admin管理系统 
		内置表单模型、Cache缓存系统、国际化系统等
		
创建Django项目:

$ django-admin startproject MyDjango

目录结构如下： 
$ find MyDjango/ 
MyDjango/ 
MyDjango/manage.py 					 命令行工具 
MyDjango/MyDjango 
MyDjango/MyDjango/__init__.py 
MyDjango/MyDjango/settings.py        项目的配置文件 
MyDjango/MyDjango/urls.py 
MyDjango/MyDjango/wsgi.py


创建Django应用程序

$ python manage.py help  查看该工具的具体功能 

$ python manage.py startapp index 

index/migrations 数据库迁移文件夹 
index/models.py  模型 
index/apps.py 当前app配置文件 
index/admin.py 管理后台 
index/tests.py 自动化测试 
index/views.py 视图



启动和停止Django应用程序


$ python manage.py  runserver 
默认是地址是127.0.0.1:8000
$ python manage.py  runserver 0.0.0.0:80(改为别的地址)
Quit the server with CONTROL-C $ CONTROL-C (停止使用ctrl + C)


Django的配置文件settings.py

配置文件包括： 
	• 项目路径 
	• 密钥 
	• 域名访问权限 
	• App 列表 
	• 静态资源，包括CSS、JavaScript 图片等 
	• 模板文件 
	• 数据库配置 
	• 缓存 
	• 中间件
	
	
URL调度器

MyDjango/urls.py 文件中的urlpatterns 列表，实现了：
从URL路由到视图(views)的映射功能 过程中使用了一个Python模块，**URLconf**(URL configuration)，
通常这个功能 也被称作URLconf

Django如何处理一个请求:

当一个用户请求Django 站点的一个页面：
1. 如果传入HttpRequest对象拥有urlconf属性（通过中间件设置），它的值
   将被用来代替 ROOT_URLCONF 设置。 
2. Django 加载URLconf模块并寻找可用的urlpatterns，Django 依次匹配每个
   URL 模式，在与 请求的URL 匹配的第一个模式停下来。 
3. 一旦有URL 匹配成功，Djagno 导入并调用相关的视图，视图会获得如下参数： 
        • 一个HttpRequest 实例 
		• 一个或多个位置参数提供 
4. 如果没有URL 被匹配，或者匹配过程中出现了异常，Django会调用一个适当的错误处理视图。

增加项目urls

from django.contrib import admin
from django.urls import path,include 

urlpatterns = [ 
    path('admin/', admin.site.urls), 
	path('',include('index.urls')), 
]


增加index的urls
# index/urls.py 
from django.urls import path 
from . import views

urlpatterns = [ 
	path('', views.index) 
]
# index/views.py 
from django.shortcuts import render 
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello Django!")
	
	
模块和包

模块：.py结尾的Python程序 
包：存放多个模块的目录 
__init__.py 包运行的初始化文件，可以是空文件

常见以下几种方式导入： 
import 
from ... import ... 
from ... import ... as ...


带变量的URL

Django 支持对URL 设置变量,URL 变量类型包括： 
• str 
• int 
• slug 
• uuid 
• path
path('<int:year>', views.myyear),

UTL的正则表达式匹配：

urls.py 
re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear’),

views.py 
def myyear(request, year): 
	return render(request, 'yearview.html')

Templates文件夹增加yearview.html 
<a href="{%  url 'urlyear' 2020 %}">2020 booklist</a></div>


view视图
 
        响应类型                                   说明 
HttpResponse(‘Hello world’)                  HTTP 状态码200，请求已成功被服务器接收 
HttpResponseRedirect(‘/admin/’)              HTTP 状态码302，重定向Admin 站点的URL 
HttpResponsePermanentRedirect(‘/admin/’)     HTTP 状态码301，永久重定向Admin站点URL 
HttpResponseBadRequest(‘BadRequest’)         HTTP 状态码400，访问的页面不存在或者请求错误 
HttpResponseNotFound(‘NotFound’)             HTTP 状态码404，页面不存在或者网页的URL失效 
HttpResponseForbidden(‘NotFound’)            HTTP 状态码403，没有访问权限 
HttpResponseNotAllowed(‘NotAllowedGet’)      HTTP 状态码405，不允许使用该请求方式 
HttpResponseSeverError(‘SeverError’)         HTTP 状态码500，服务器内容错误


Django快捷函数:
render() 将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个 HttpResponse 对象。
redirect() 将一个HttpResponseRedirect 返回到传递的参数的适当URL。
get_object_or_404() 在给定的模型管理器( model manager) 上调用get() ，但它会引发Http404 而不是 模型的DoesNotExist 异常。

基于类的视图：

在视图函数里处理HTTP GET 的代码应 该像下面这样： 
from django.http import HttpResponse

def my_view(request): 
	if request.method == 'GET': 
		# <view logic> 
		return HttpResponse('result')
		

而在基于类的视图里，会变成：
from django.http import HttpResponse 
from django.views import View

class MyView(View): 
	def get(self, request): 
		# <view logic> 
		return HttpResponse('result’)
		
模型与数据库：

• 每个模型都是一个Python 的类，这些类继承django.db.models.Model 
• 模型类的每个属性都相当于一个数据库的字段 
• 利用这些，Django提供了一个自动生成访问数据库的API

from django.dbimport models 

class Person(models.Model): 
	id = models.IntegerField(primary_key=True) 
	first_name= models.CharField(max_length=30) 
	last_name= models.CharField(max_length=30)

对应SQL：
CREATE TABLE myapp_person( 
	"id" serial NOT NULL PRIMARY KEY, 
	"first_name" varchar(30) NOT NULL, 
	"last_name" varchar(30) NOT NULL );
	
生成表的命令：
$ python manage.py makemigrations
更新修改表的命令： 
$ python manage.py migrate


字段：
字段类型 模型中每一个字段都应该是某个Field 类的实例
字段选项 每一种字段都需要指定一些特定的参数
参考：https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/

关联关系:
• 多对一 
• 多对多 
• 一对一

查询：

执行查询常见方法： 
• save() • add() • all() • filter() • get()

模板:
jieba库：
• jieba分词与提取关键词 
• jieba调整词典 
• jieba词性标注

URLconf的处理:
http://ip/xxx 
http://ip/yyy 
http://ip/douban/xxx 
http://ip/douban/yyy 
将URL中的douban/注册成一个独立的APP

setting.py的处理:
• 注册APP 
INSTALLED_APPS=[Douban] 
• 数据库 
DATABASES = { 
... ... 
}

模型的处理:
• 从Django到SQL 
    • python manage.py migrate 

• 从SQL到Django 
    • python manage.py inspectdb

视图的处理:
• objects.all()  #选取所有数据 
• objects.all().count()  #计数 
• objects.values('n_star')#某一列数据 
• queryset.filter(**condtions).count() #符合条件计数

manage.py做了些什么?

1. 解析manage.py 的runserver 和IP端口参数 
2. 找到command 目录加载runserver.py 
3. 检查INSTALL_APP、IP地址、端口、ORM对象 
4. 实例化wsgiserver 
5. 动态创建类并接收用户的请求


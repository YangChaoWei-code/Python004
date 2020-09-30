学习笔记
一.爬取网页数据用到的库，三方的request和自带的urllib库，urllib使用起来比较繁琐，建议
使用request

使用request爬取网页数据的大致步骤(无需登录账号的方式):
1.import requests
2.  user_agent = ''
    cookie = ''
    header = {'user-agent':user_agent, 'cookie':cookie}
3.response = requests.get(url, headers = header)

二.解析爬取到的网页数据所用到的库,BeautifulSoup 或 lxml.etree, 其中使用lxml.etree解析
效率要比BeautifulSoup快很多

使用BeautifulSoup解析网页数据的大致方式:

from bs4 import BeautifulSoup as bs
bs_info = bs(response.text, 'html.parser')
接下来根据指定元素来提取bs_info对应的值，具体参考:
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/


使用lxml.etree解析网页数据的大致方式:
import lxml.etree
selector = lxml.etree.HTML(response.text)
data = selector.xpath('该内容可以复制网页上的或者自己定义')
参考链接：
Scrapy Xpath 官方学习文档： https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths 
Xpath 中文文档：https://www.w3school.com.cn/xpath/index.asp 
Xpath 英文文档：https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf

三.使用scrapy框架爬虫

创建简单爬虫项目的大致步骤:
1.创建爬虫项目：scrapy startproject + 项目名字
2.在爬虫项目中创建一个要爬取的小项目:进入到项目名字目录 scrapy genspider + name(运行时需要用到) + 域名
3.添加爬虫代码，主要逻辑:name.py,需要修改的其他文件(settings.py、pipelines.py、items.py) 注意：不要随意修改爬虫项目名
4.运行爬虫程序:scrapy crawl name

四. 使用pandas库生成csv文件,自带的csv库也可以使用但是效率没有pandas高

import pandas as pd
movie = pd.DataFrame(data=movie)
movie.to_csv('./maoyan_movies.csv',encoding='utf8', index=False, header=False)
学习笔记

异常捕获：
参考https://docs.python.org/zh-cn/3.6/library/exceptions.html 
所有内置的非系统退出的异常都派生自Exception 类
StopIteration异常示例： 
	gennumber = ( i for i in range(0,2)) print(next(gennumber)) 
	print(next(gennumber)) 
	try: 
		print(next(gennumber)) 
	except StopIteration: 
		print('后一个元素')



异常处理机制的原理:

• 异常也是一个类 
• 异常捕获过程
	1.异常类把错误消息打包到一个对象 
	2.然后该对象会自动查找到调用栈 
	3.直到运行系统找到明确声明如何处理这些类异常的位置
• 所有异常继承自BaseException 
• Traceback显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的


异常信息与异常捕获:
• 异常信息在Traceback信息的后一行，有不同的类型 
• 捕获异常可以使用try…except语法 
• try…except支持多重异常处理

常见的异常类型主要有： 
	1.LookupError下的IndexError和KeyError 
	2.IOError 
	3.NameError 
	4.TypeError 
	5.AttributeError 
	6.ZeroDivisionError

抛出异常和自定义异常

	使用raise语句抛出异常 
	自定义异常建议从Exception继承
	
使用pymysql基本操作:
import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '',
    database = 'testdb',
    charset = 'utf8mb4'
)

# 获得cursor游标对象
con1 = conn.cursor()

# 操作的行数
count = con1.execute('select * from role;')
# print(f'查询到{count}条记录')

# 获得一条查询结果
result = con1.fetchone()
# print(result)

# 获得所有查询结果(注意：如果执行了con1.fetchone(),那所有的就是剩下的那些结果)
print(con1.fetchall())
con1.close()

#执行批量插入
try:
    values = [(id, 'pyuser'+ str(id)) for id in range(4, 21)]
    print(values)
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
       cursor.executemany("INSERT INTO pyuser VALUES (%s, %s)", values)
    conn.commit()

finally:
    conn.close()
	
反爬虫:

1.模拟头部信息
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

# 模拟不同浏览器
print(f'Chrome浏览器: {ua.chrome}')

# 随即返回头部信息，推荐使用
print(f'随机浏览器: {ua.random}')

2.模拟登陆
可以使用request或者webdriver库，详见作业二

3.验证码识别
# 先安装依赖库libpng, jpeg, libtiff, leptonica
# brew install leptonica
# 安装tesseract
# brew install  tesseract
# 与python对接需要安装的包
# pip3 install Pillow
# pip3 install pytesseract

其中window系统需要安装：
tesseract
# pip3 install Pillow
# pip3 install pytesseract

# 各种语言识别库 https://github.com/tesseract-ocr/tessdata

大致步骤：(目前适用于英文字母验证)
from PIL import Image
import pytesseract

# 下载图片
# session = requests.session()
# img_url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1320441599,4127074888&fm=26&gp=0.jpg'
# agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# headers = {'User-Agent': agent}
# r = session.get(img_url, headers=headers)

# with open('cap.jpg', 'wb') as f:
#     f.write(r.content)

# 打开文件
im = Image.open('cap.jpg')

# 灰度图片
gray = im.convert('L')
gray.save('c_gray2.jpg')
im.close()

# 二值化
threshold = 100
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('c_th.jpg')

th = Image.open('c_th.jpg')
#输出验证码内容
print(pytesseract.image_to_string(th,lang='chi_sim+eng'))


Scrapy的中间件:


如何编写一个下载中间件？一般需要重写下面四个主要方法： 

process_request(request, spider) 
Request 对象经过下载中间件时会被调用，优先级高的先调用 

process_response(request, response, spider) 
Response对象经过下载中间件时会被调用，优先级高的后调用 

process_exception(request, exception, spider) 
当process_exception() 和process_request() 抛出异常时会被调用 

from_crawler(cls, crawler) 
使用crawler 来创建中间器对象，并（必须）返回一个中间件对象


还需要 ：更换代理IP 更换Cookies 更换User-Agent 自动重试


分布式爬虫:

Scrapy原生不支持分布式，多机之间需要Redis实现队列和管道的共享。 
scrapy-redis很好地实现了Scrapy和Redis的集成

使用scrapy-redis之后Scrapy的主要变化： 
1. 使用了RedisSpider类替代了Spider类 
2. Scheduler的queue由Redis实现 
3. item pipeline由Redis实现

安装并启动：pip install scrapy-redis

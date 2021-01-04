毕业项目：构建一个舆情分析平台

项目背景：某公司计划新上线一款苏打水饮料，为了了解用户对苏打水的接受程度，需要抓取“什么值得买”( https://www.smzdm.com/fenlei/qipaoshui/ ) 
网站中气泡水种类前 10 的产品的用户评论，通过对用户评论的正向、负向评价了解排名前 10 的气泡水产品的用户接受程度。

注意：
由于这个网站的产品是实时更新的，一些新的气泡水产品可能没有足够数量的评论，大家可以将气泡水替换为其他产品，比如：

手机产品 24 小时排行 https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/
电脑游戏最新排行 https://www.smzdm.com/fenlei/diannaoyouxi/
洗发护发产品 24 小时排行 https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/
具体需求：

正确使用 Scrapy 框架或 Selenium 获取评论，如果评论有多页，需实现自动翻页功能，将原始评论结果存入 MySQL 数据库，并使用定时任务每天定期更新。
对评论数据进行清洗（可借助 Pandas 库），并进行语义情感分析，将分析结果存入数据库。
使用 Django 集成在线图表对采集数、舆情进行展示，需包括该产品正、负评价比例，以及评价内容等。
数据展示支持按时间筛选和按关键词筛选功能（参考）
https://www.yqt365.com/newEdition/wb/event/analysis/w1yqtxwb62574190201152403817


本次项目作业我选取的是手机产品：https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/

我的作业中目前已有的功能：
	1.使用 Scrapy获取评论，实现自动翻页功能
	2.使用 snownlp对评论进行情感分析，并和原始数据一起存入到MySQL 数据库
	3.使用 Django对数据进行展示，包括该产品正、负评价比例，以及评价内容，价格，产品名及描述
	4.实现按照产品名进行筛选的功能
余下的功能持续更新。。。



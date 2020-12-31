# -*- coding: utf-8 -*-

# Scrapy settings for comment project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'comment'

SPIDER_MODULES = ['comment.spiders']
NEWSPIDER_MODULE = 'comment.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'comment (+http://www.yourdomain.com)'
# USER_AGENT_LIST=[
# 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
# ]
# import random
# USER_AGENT = random.choice(USER_AGENT_LIST)
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
REDIRECT_ENABLED = False                       # 关掉重定向, 不会重定向到新的地址
HTTPERROR_ALLOWED_CODES = [301, 302]
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
cookie = '__ckguid=na52SbgUjFJAYR3c1e5QNh; __jsluid_s=ee07e46b955b23dccfadf8327b02e2de; device_id=19612773601608642728870039e117a59d01a25f821a7cb872197b2ad3; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F52%3Farticle%3D273014%26utm_source%3Dwechat%26utm_medium%3DKFQA%26utm_term%3DKFQA%26gk_cus_user_wechat%3Duniversity%22%7D; _ga=GA1.2.756184741.1608642730; wt3_sid=%3B999768690672041; smzdm_ec=06; smzdm_ea=200; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F52%3Farticle%3D273014%26utm_source%3Dwechat%26utm_medium%3DKFQA%26utm_term%3DKFQA%26gk_cus_user_wechat%3Duniversity%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2Ffenlei%2Fzhinengshouji%2Fh5c4s0f0t0p1%2F%23feed-main%2F%22%7D%2C%22%24device_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%7D; _gid=GA1.2.1005676141.1608901637; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1608725231,1608901717,1608966401,1608966405; __jsluid_h=452d6389aaf907afbea4a56e5bf4f7e8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F52%3Farticle%3D273014%26utm_source%3Dwechat%26utm_medium%3DKFQA%26utm_term%3DKFQA%26gk_cus_user_wechat%3Duniversity%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2Ffenlei%2Fzhinengshouji%2Fh5c4s0f0t0p1%2F%23feed-main%2F%22%7D%2C%22%24device_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%7D; _gat_UA-27058866-1=1; wt3_eid=%3B999768690672041%7C2160864334200416468%232160896856200987858; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1608968563; amvid=3704e1eea1b59781ee13c376ef53a266; _gat_gtag_UA_166809101_2=1; __gads=ID=b2280957ffb48cb4-22dd327557c5007f:T=1608968562:RT=1608968562:S=ALNI_Ma17TwObrVczGjUDlPcCS47yDlYAg'
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'www.smzdm.com',
    'Referer':' https://www.smzdm.com/fenlei/zhinengshouji/',
    'Sec-Fetch-Dest': 'document',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Cookie': '__ckguid=na52SbgUjFJAYR3c1e5QNh; __jsluid_s=ee07e46b955b23dccfadf8327b02e2de; device_id=19612773601608642728870039e117a59d01a25f821a7cb872197b2ad3; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F52%3Farticle%3D273014%26utm_source%3Dwechat%26utm_medium%3DKFQA%26utm_term%3DKFQA%26gk_cus_user_wechat%3Duniversity%22%7D; _ga=GA1.2.756184741.1608642730; wt3_sid=%3B999768690672041; smzdm_ec=06; smzdm_ea=200; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F52%3Farticle%3D273014%26utm_source%3Dwechat%26utm_medium%3DKFQA%26utm_term%3DKFQA%26gk_cus_user_wechat%3Duniversity%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2Ffenlei%2Fzhinengshouji%2Fh5c4s0f0t0p1%2F%23feed-main%2F%22%7D%2C%22%24device_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%7D; _gid=GA1.2.1005676141.1608901637; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1608725231,1608901717,1608966401,1608966405; __jsluid_h=452d6389aaf907afbea4a56e5bf4f7e8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F52%3Farticle%3D273014%26utm_source%3Dwechat%26utm_medium%3DKFQA%26utm_term%3DKFQA%26gk_cus_user_wechat%3Duniversity%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2Ffenlei%2Fzhinengshouji%2Fh5c4s0f0t0p1%2F%23feed-main%2F%22%7D%2C%22%24device_id%22%3A%221768a9417601c4-04c21dc30b2aaf-c781f38-1327104-1768a941761874%22%7D; _gat_UA-27058866-1=1; wt3_eid=%3B999768690672041%7C2160864334200416468%232160896856200987858; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1608968563; amvid=3704e1eea1b59781ee13c376ef53a266; _gat_gtag_UA_166809101_2=1; __gads=ID=b2280957ffb48cb4-22dd327557c5007f:T=1608968562:RT=1608968562:S=ALNI_Ma17TwObrVczGjUDlPcCS47yDlYAg',
    'Cache-Control': 'max-age=60'
    }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'comment.middlewares.CommentSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'comment.middlewares.CommentDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'comment.pipelines.CommentPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

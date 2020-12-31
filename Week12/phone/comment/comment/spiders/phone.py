# -*- coding: utf-8 -*-
import scrapy
from snownlp import SnowNLP
from myProject.phone.comment.comment.items import CommentItem
from scrapy.selector import Selector
import re

class PhoneSpider(scrapy.Spider):
    name = 'phone' # 运行爬虫时的名字 scrapy crawl phone
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

    def start_requests(self):
        start_url = f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/'
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        links = Selector(response=response).xpath('//div[@class="feed-block z-hor-feed"]//div/h5/a/@href').extract()
        print("links:", end="")
        print(links)
        for link in links[:10]:
            yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        quchong = set()
        page_next = Selector(response=response).xpath('//div[@class="tab_info"]/ul[@class="pagination"]/li/a/@href').extract()
        if page_next:
            print('page_next:', end="")
            print(page_next)
            for i in page_next:
                if 'https' in i and i not in quchong:
                    quchong.add(i)
                    yield scrapy.Request(url=i, callback=self.parse3)
        else:
            item = CommentItem()
            product_name = Selector(response=response).xpath('//*[@id="feed-wrap"]/div/a/span/text()').extract()
            description = Selector(response=response).xpath('//div[@class="title-box"]/h1/text()').extract()
            price = Selector(response=response).xpath('//div[@class="title-box"]/div/span/text()').extract()
            data = Selector(response=response).xpath('//div[@class="comment_con"]/p/span/text()[1]').extract()
            if data:
                for i in data:
                    line_content = i.strip()
                    if line_content:
                        item['content'] = line_content
                        item['product_name'] = ''.join(product_name[-1]).strip()
                        item['description'] = fliter_str(description)
                        item['price'] = _price(price)
                        item['sentiment'] = _sentiment(line_content)
                        yield item

    def parse3(self, response):
        item = CommentItem()
        product_name = Selector(response=response).xpath('//*[@id="feed-wrap"]/div/a/span/text()').extract()
        description = Selector(response=response).xpath('//div[@class="title-box"]/h1/text()').extract()
        price = Selector(response=response).xpath('//div[@class="title-box"]/div/span/text()').extract()
        data = Selector(response=response).xpath('//div[@class="comment_con"]/p/span/text()[1]').extract()
        if data:
            for i in data:
                line_content = i.strip()
                if line_content:
                    item['content'] = line_content
                    item['product_name'] = ''.join(product_name[-1]).strip()
                    item['description'] = fliter_str(description)
                    item['price'] = _price(price)
                    item['sentiment'] = _sentiment(line_content)
                    yield item


def fliter_str(s):
    new_s = ''.join(s).strip()
    return new_s.replace(' ', '')


def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments


def _price(price):
    price_str = ''.join(price).strip()
    reg = '\d+'
    phone_price = re.search(reg, price_str)
    if phone_price:
        return phone_price.group(0)
    else:
        return
if __name__ == '__main__':
    import os
    os.system("scrapy crawl phone")
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MoivesSpider(scrapy.Spider):
    name = 'moives'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'

        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        print(response.url)
        data = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        item = SpidersItem()
        movie = []
        item['movie'] = movie
        for tags in data[:10]:
            name = tags.xpath('./div[@class="movie-hover-title"][1]/span[1]/text()').extract_first().strip()
            tag = tags.xpath('./div[@class="movie-hover-title"][2]/text()')[1].extract().strip()
            start_time = tags.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].extract().strip()
            movie.append((name,tag,start_time))
        yield item

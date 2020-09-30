# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class SpidersPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        movie = item['movie']
        movie = pd.DataFrame(data=movie, columns=['电影名', '类型', '上映时间'])
        movie.to_csv('./maoyan_movies.csv',encoding='utf8', index=False, header=False)
        return item
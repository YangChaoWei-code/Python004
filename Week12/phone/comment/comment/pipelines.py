# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class CommentPipeline:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', passwd='', db='testdb', charset='utf8mb4',
                                  port=3306)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO phonecomment_phonecomment(`product_name`,`description`,`price`,`content`, `sentiment`) VALUES(%s,%s,%s,%s,%s) '
        self.cur.execute(sql,
                         (item['product_name'], item['description'], item['price'], item['content'], item['sentiment']))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '',
    database = 'testdb',
    charset = 'utf8mb4'
)

class SpidersPipeline:
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        movie = item['movie']
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.executemany("INSERT INTO moives VALUES (%s, %s, %s)", movie)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return item
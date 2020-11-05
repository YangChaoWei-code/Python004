# -*- coding:utf-8 -*-
"""
@author:YCW
@file:douban_content.py
@time:2020/11/3 0:39
"""
import requests
import lxml.etree
import pymysql


def get_url_name(myurl, count):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    cookie = 'bid=LWddXIJkHGc; __utma=30149280.1922422879.1584108885.1584108885.1584108885.1; ll="108296"; _vwo_uuid_v2=D2D0F16845CD28AA6CE7F6F4D2133E896|04ffa3de34a65c3c4a3fa1b48481e393; push_noty_num=0; push_doumail_num=0; __yadk_uid=WEbTwj51VIvlSksMJnHwjkbq3TALZIGO; __gads=ID=745de04c8116e896:T=1604335073:S=ALNI_MbPmV2sPiwoKWoC-Y5oRhIIHmiEFQ; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1604424974%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=2a6a3a8bcd7a0d3d.1601225209.5.1604425029.1604335239.'
    header = {'user-agent':user_agent, 'cookie':cookie}
    response = requests.get(myurl, headers = header)
    selector = lxml.etree.HTML(response.text)

    data = selector.xpath('//div[@class="comment"]')
    save_data = []
    print(type(data))
    stars = {'很差': 1, '较差': 2, '还行': 3, '推荐': 4, '力荐': 5}
    for tags in data:
        count = count + 1
        if tags.xpath('./h3/span[2]/span[3]'):
            star = tags.xpath('./h3/span[2]/span[2]/@title')
            comment = tags.xpath('./p/span/text()')
            res = [count, comment, stars[''.join(star)]]
            save_data.append(res)
    return save_data


if __name__ == '__main__':
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='',
        password='',
        database='testdb',
        charset='utf8mb4'
    )
    try:
        for i in range(0, 200, 20):
            if i == 0:
                url = f'https://movie.douban.com/subject/1292720/comments?sort=new_score&status=P'
            else:
                url = 'https://movie.douban.com/subject/1292720/comments?start=' + str(i) +'&limit=20&status=P&sort=new_score'
            movies = get_url_name(url, i)
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.executemany("INSERT INTO douban_douban VALUES (%s, %s, %s)", movies)
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

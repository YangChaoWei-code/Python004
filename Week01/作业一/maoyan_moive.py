# -*- coding:utf-8 -*-
"""
@author:YCW
@file:maoyan_moive.py
@time:2020/9/2822:03
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    cookie = '__mta=188125463.1601301901466.1601302306024.1601302379779.9; ' \
             'uuid_n_v=v1; uuid=ECF934A0019211EB8A3FF31971B0D6F038B0AB428AB34E12B3566536F67293AF; ' \
             '_csrf=2c649957050d6f89b773981009c45cc3026fa3d5439e7ae0f5b447424caed68c;' \
             ' _lxsdk_cuid=174d503e42686-08c0023a892e41-8383268-144000-174d503e428c8; ' \
             '_lxsdk=ECF934A0019211EB8A3FF31971B0D6F038B0AB428AB34E12B3566536F67293AF; ' \
             'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601301643; ' \
             'mojo-session-id={"id":"f9c10d2b66a0dfc5c8e771453e7f7e6c","time":1601301646017}; ' \
             'mojo-uuid=33d8eab14967cce112115b138a4750a9; mojo-trace-id=44; ' \
             'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601305135; ' \
             '__mta=188125463.1601301901466.1601302379779.1601305137366.10; ' \
             '_lxsdk_s=174d52ab611-288-7da-bda%7C%7C12'
    header = {'user-agent':user_agent, 'cookie':cookie}
    response = requests.get(myurl, headers = header)
    bs_info = bs(response.text, 'html.parser')
    data = bs_info.find_all('dd')[:10]
    save_data = []

    for tags in data:
        name = tags.find('span', attrs={'class':'name'}).text
        tag = tags.find('div', attrs={'class':'movie-hover-info'}).select('div')[1].get_text()\
              .replace('类型:', '').replace(' ','').replace('\n', '')
        start_time = tags.find('div', attrs={'class':'movie-hover-info'}).select('div')[3].get_text()\
              .replace('上映时间:', '').replace(' ','').replace('\n', '')
        res = [name, tag, start_time]
        save_data.append(res)
    return save_data


if __name__ == '__main__':
    url = f'https://maoyan.com/films?showType=3'
    movies = get_url_name(url)
    movies.insert(0,['电影名', '类型', '上映时间'])
    movie = pd.DataFrame(data=movies)
    movie.to_csv('./maoyan_movies.csv', encoding='utf8', index=False, header=False)

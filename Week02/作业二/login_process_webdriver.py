# -*- coding:utf-8 -*-
"""
@author:YCW
@file:login_process_webdriver.py
@time:2020/10/813:43
"""
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://processon.com/login?f=index')
    #time.sleep(1)

    #browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    # btm1 = browser.find_element_by_xpath('/html/body/header/ul/li[5]/a')
    # btm1.click()

    browser.find_element_by_xpath('//input[@name="login_email"]').send_keys('')
    browser.find_element_by_xpath('//input[@id="login_password"]').send_keys('')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="signin_btn"]').click()
    time.sleep(3)
    # browser.find_element_by_xpath('//*[@id="new-file"]').click()
    # time.sleep(3)
    # browser.find_element_by_xpath('/html/body/div[4]/div[1]/span[2]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)


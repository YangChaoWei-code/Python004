# -*- coding:utf-8 -*-
"""
@author:YCW
@file:homework.py
@time:2020/12/5 12:55
"""
import time
# 作业一：
#
# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
#
# list
# tuple
# str
# dict
# collections.deque
# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。
#
# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

# 作业一：
# 容器序列 list tuple collections.deque
# 扁平序列 str
# 可变序列 list collections.deque
# 不可变序列 tuple str
# 非序列 dict


# 作业二：自定义一个 python 函数，实现 map() 函数的功能。
def my_map(func, *args, **kwargs):
    return func(*args, **kwargs)


a = my_map(sum, [1, 2])
print(a)


# 作业三：
def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} execute time is {end - start}s.')
        return res
    return inner


@timer
def my_map(func, *args, **kwargs):
    return func(*args, **kwargs)


a = my_map(sum, [1, 2])
print(a)

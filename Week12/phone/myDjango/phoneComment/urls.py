# -*- coding:utf-8 -*-
"""
@author:YCW
@file:urls.py
@time:2020/12/28 22:37
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search)
]

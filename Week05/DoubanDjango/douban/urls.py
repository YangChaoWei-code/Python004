# -*- coding:utf-8 -*-
"""
@author:YCW
@file:urls.py
@time:2020/11/1 22:29
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search)
]
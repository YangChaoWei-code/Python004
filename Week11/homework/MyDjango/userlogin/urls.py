# -*- coding:utf-8 -*-
"""
@author:YCW
@file:urls.py
@time:2020/12/20 22:05
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login)
]
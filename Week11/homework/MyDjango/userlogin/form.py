# -*- coding:utf-8 -*-
"""
@author:YCW
@file:form.py
@time:2020/12/20 22:08
"""
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
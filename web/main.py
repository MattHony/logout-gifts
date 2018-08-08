# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/2 21:08
# @Author : '红文'
# @File : main.py
# @Software: PyCharm
from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('personal')
def personal_center():
    pass

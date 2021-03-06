# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/8 20:00
# @Author : '红文'
# @File : gift.py
# @Software: PyCharm
from .book import BookViewModel
from collections import namedtuple

MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []

        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['count']:
                count = wish_count['count']
        my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        return my_gift
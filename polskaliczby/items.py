# -*- coding: utf-8 -*-
#
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StackItem(Item):
    Wojewodztwo = Field()
    Populacja = Field()
    Obszar = Field()
    Stopa_urbanizacji = Field()

# from scrapy.item import Item, Field
#
#
# class StackItem(Item):
#     title = Field()
#     url = Field()

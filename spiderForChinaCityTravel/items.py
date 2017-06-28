# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class SpiderforchinacitytravelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class articleInfoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # md5_url=Field()
    url=Field()
    originUrl=Field()
    originName=Field()
    title=Field()
    keywords=Field()
    abstracts=Field()
    content=Field()
    type=Field()
    group=Field()
    status=Field()
    pageUrls=Field()
    pass
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoparoundItem(scrapy.Item):
    # define the fields for your item here like:
    store_names = scrapy.Field()
    shop_names = scrapy.Field()
    sale_volumes = scrapy.Field()
    prices = scrapy.Field()
    shop_urls = scrapy.Field()
    pic_urls = scrapy.Field()
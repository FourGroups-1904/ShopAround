# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    store_names = scrapy.Field()
    shop_names = scrapy.Field()
    prices = scrapy.Field()
    shop_urls = scrapy.Field()
    pic_urls = scrapy.Field()
    search_name = scrapy.Field()


class YhdItem(scrapy.Item):
    store_names = scrapy.Field()  # 店铺名字
    shop_names = scrapy.Field()  # 商品名字
    prices = scrapy.Field()  # 价格
    shop_urls = scrapy.Field()  # 商品url
    pic_urls = scrapy.Field()  # 图片url
    search_name = scrapy.Field()  # 关键字
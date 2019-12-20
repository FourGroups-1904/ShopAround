# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoparoundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    store_names = scrapy.Field()  # 店铺名字
    shop_names = scrapy.Field()  # 商品名字
    sale_volumes = scrapy.Field()  # 销量
    prices = scrapy.Field()  # 价格
    shop_urls = scrapy.Field()  # 商品url
    pic_urls = scrapy.Field()  # 图片url

# -*- coding: utf-8 -*-
import scrapy
from ShopAround.items import ShoparoundItem
import re
import time


class TaobaoSpider(scrapy.Spider):
    name = 'yhd'
    allowed_domains = ['yhd.com']
    keyword_name = input('请输入需要搜索的名称')
    start_urls = ['https://search.yhd.com/c0-0/k' + keyword_name, ]
    print(start_urls)

    def parse(self, response):
        item = ShoparoundItem()
        html = response.text
        print(html)
        store_names_s = re.findall('<span class="shop_text">(.*?)</span>', html)  # 店铺名字
        shop_names_s = re.findall('title="(.*?)" singleFreeFlag="0"',html) # 商品名字
        sale_volumes_s = re.findall('<i class="iconSearch">&#xe614;</i>(.*?)</a>', html)  # 销量
        prices_s = re.findall('yhdPrice="(.*?)"', html)  # 价格
        shop_urls_s = re.findall('href="(.*?)" target="_blank" isSeiralCombine="0"', html)  # 商品url
        pic_urls_s = response.xpath('//div[@class="proImg"]/a/img/@src')  # 图片url
        print('--->>>>', shop_names_s,sale_volumes_s,prices_s,shop_urls_s,pic_urls_s)

        # print('测试直接div一个模块:',ceshi1[0].get('data-href'))
        # store_name_s = response.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/span[2]/text()').getall()
        # trade_name_s = response.xpath().getall()
        # Sales_s = response.xpath().getall()
        # price_s = response.xpath().getall()
        # trade_url_s = response.xpath().getall()
        # img_url_s = response.xpath().getall()
        yield item

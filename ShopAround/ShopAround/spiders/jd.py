# -*- coding: utf-8 -*-
import scrapy
from ShopAround.items import ShoparoundItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    # serach_name = input('你输入想要查询的商品名称: ')
    # for page in range(1, 3):
    #     page = 1 + (page-1)*2
    #     start_urls = [f'https://search.jd.com/Search?keyword={serach_name}&enc=utf-8&page={page}']
    start_urls = ['https://search.jd.com/Search?keyword=手机&enc=utf-8&page=13']

    def parse(self, response):
        item = ShoparoundItem()
        item['store_names'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-shop"]/span/a/@title').getall()
        item['shop_names'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-name p-name-type-2"]/a/em/text()').getall()
        item['sale_volumes'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-commit"]/strong/a/text()').getall()
        item['prices'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-price"]/strong/i/text()').getall()
        item['shop_urls'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/img/@src').getall()
        item['pic_urls'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/@href').getall()
        yield item

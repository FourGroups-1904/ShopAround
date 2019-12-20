# -*- coding: utf-8 -*-
import scrapy
from ShopAround.items import KaolaoItem

class KaolaoSpider(scrapy.Spider):
    name = 'kaolao'
    allowed_domains = ['search.kaolao.com']
    search_name = input('你输入想要查询的考拉商品名称: ')
    page = int(input('你输入想要爬取考拉的商品页数: '))
    start_urls = [f'https://search.kaola.com/search.html?key={search_name}&pageNo={page}']

    def parse(self, response):
        """
 store_names= response.xpath('//*[@id="result"]/li[1]/div/div[2]/p[4]/a/text()').getall()
 shop_names= response.xpath('//*[@id="result"]/li[1]/div/div[2]/div/a/h2/text()').getall()
 prices = response.xpath('//*[@id="result"]/li[1]/div/div[2]/p[1]/span[1]/text()').getall()
 shop_urls = response.xpath('//*[@id="result"]/li/div/a/@href').getall()
 pic_urls = response.xpath('//*[@id="result"]/li/div/a/div/img/@data-src').getall()
 response.xpath('//*[@id="result"]/li/div/a/@title').getall()
 //*[@id="result"]/li[37]/div/a/@title
        """
        search_name = []
        pic_urls_s = []
        shop_urls_s = []
        kaolao_item = KaolaoItem()
        kaolao_item['store_names'] = response.xpath('//*[@id="result"]/li/div/div/p[4]/a/text()').getall()
        kaolao_item['shop_names'] = response.xpath('//*[@id="result"]/li/div/a/@title').getall()
        kaolao_item['prices'] = response.xpath('//*[@id="result"]/li/div/div[2]/p[1]/span[1]/text()').getall()

        shop_urls = response.xpath('//*[@id="result"]/li/div/a/@href').getall()
        for i in shop_urls:
            shop_urls_s.append('https:' + i)
        kaolao_item['shop_urls'] = shop_urls_s

        pic_urls = response.xpath('//*[@id="result"]/li/div/a/div/img/@data-src').getall()
        for i in pic_urls:
            pic_urls_s.append('https:' + i)
        for i in range(len(kaolao_item['shop_urls'])):
            search_name.append(self.search_name)
        kaolao_item['pic_urls'] = pic_urls_s
        kaolao_item['search_name'] = search_name

        yield kaolao_item

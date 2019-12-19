# -*- coding: utf-8 -*-
import scrapy

# from scrapyMysql.items import ScrapymysqlItem

# scrapy shell http://lab.scrapyd.cn/
class InputmysqlSpider(scrapy.Spider):
    name = 'inputMysql'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        mingyan = response.css('div.quote')
        # mingyan = response.xpath('//div[@class="quote post"]//span[@class="text"]//text()').getall()
        item = ScrapymysqlItem()
        for v in mingyan:
            item['cont'] = v.css('.text::text').extract_first()  # 提取名言
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            item['tag'] = ','.join(tags)  # 数组转化为字符串
            yield item  # 把取到的数据交给pipeline处理
        next_page = response.css('li.next a::attr(href)').extract_first()  # css 选择器提取下一页链接
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 提交给parse继续抓取下一页



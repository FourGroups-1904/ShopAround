# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
from ShopAround.items import JdItem, YhdItem
from ShopAround.config import username, pwd

class ShoparoundPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='shoparound',
            user=username,
            passwd=pwd,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    # def process_item(self, item, spider):
    #
    #     if isinstance(item, JdItem):
    #         for i in range(len(item['shop_urls'])):
    #             self.cursor.execute(
    #             """insert into jd(store_names, shop_names, prices, shop_urls, pic_urls, search_name)
    #             value (%s, %s, %s, %s, %s, %s)""",
    #             (item['store_names'][i],  # item里面定义的字段和表字段对应
    #              item['shop_names'][i],
    #              item['prices'][i],
    #              item['shop_urls'][i],
    #              item['pic_urls'][i],
    #              item['search_name'][i]))
    #             self.connect.commit() # 提交
    #         return item
    #     elif isinstance(item, YhdItem):
    #         for i in range(len(item['store_names'])):
    #             self.cursor.execute(
    #                 """insert into yhd(store_names, shop_names, prices, shop_urls, pic_urls,search_name)
    #                 value (%s, %s, %s, %s, %s, %s)""",
    #                 (item['store_names'][i],  # item里面定义的字段和表字段对应
    #                  item['shop_names'][i],
    #                  item['prices'][i],
    #                  item['shop_urls'][i],
    #                  item['pic_urls'][i],
    #                  item['search_name'][i]))
    #             self.connect.commit()  # 提交
    #         return item
    def process_item(self, item, spider):

        if isinstance(item, JdItem):
            for i in range(len(item['shop_urls'])):
                self.cursor.execute(
                """insert into jd(store_names, shop_names, prices, shop_urls, pic_urls, search_name)
                value (%s, %s, %s, %s, %s, %s)""",
                (item['store_names'][i],  # item里面定义的字段和表字段对应
                 item['shop_names'][i],
                 item['prices'][i],
                 item['shop_urls'][i],
                 item['pic_urls'][i],
                 item['search_name'][i]))
                self.connect.commit() # 提交
            return item
        elif isinstance(item, YhdItem):
            for i in range(len(item['store_names'])):
                self.cursor.execute(
                    """insert into yhd(store_names, shop_names, prices, shop_urls, pic_urls,search_name)
                    value (%s, %s, %s, %s, %s, %s)""",
                    (item['store_names'][i],  # item里面定义的字段和表字段对应
                     item['shop_names'][i],
                     item['prices'][i],
                     item['shop_urls'][i],
                     item['pic_urls'][i],
                     item['search_name'][i]))
                self.connect.commit()  # 提交
            return item

    def close_spider(self, spider):
        self.connect.close()

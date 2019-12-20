#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pymysql.cursors
from ShopAround.config import username, pwd


class YhdPipeline(object):
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

    def process_item(self, yhd_item, spider):
        for i in range(len(yhd_item['store_names'])):
            self.cursor.execute(
                """insert into yhd(store_names, shop_names, prices, shop_urls, pic_urls,search_name)
                value (%s, %s, %s, %s, %s, %s)""",
                (yhd_item['store_names'][i],  # item里面定义的字段和表字段对应
                 yhd_item['shop_names'][i],
                 yhd_item['prices'][i],
                 yhd_item['shop_urls'][i],
                 yhd_item['pic_urls'][i],
                 yhd_item['search_name'][i]))

            self.connect.commit()  # 提交
        return yhd_item

    def close_spider(self, spider):
        self.connect.close()

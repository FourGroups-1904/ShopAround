#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pymysql.cursors
from ShopAround.config import username, pwd


class JdPipeline(object):
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

    def process_item(self, jd_item, spider):
        # self.cursor.execute("SET @@global.sql_mode=''")  # 不使用严格模式
        for i in range(len(jd_item['shop_urls'])):
            self.cursor.execute(
                """insert into jd(store_names, shop_names, prices, shop_urls, pic_urls, search_name)
                value (%s, %s, %s, %s, %s, %s)""",
                (jd_item['store_names'][i],  # item里面定义的字段和表字段对应
                 jd_item['shop_names'][i],
                 jd_item['prices'][i],
                 jd_item['shop_urls'][i],
                 jd_item['pic_urls'][i],
                 jd_item['search_name'][i]))
            self.connect.commit()  # 提交
        return jd_item

    def close_spider(self, spider):
        self.connect.close()

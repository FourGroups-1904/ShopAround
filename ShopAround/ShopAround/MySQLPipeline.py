#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/12/15 10:34:22
# @License :   (C) Copyright 2019, {python_1904}


import pymysql.cursors
from ShopAround.config import username, pwd
class MySQLPipeline(object):
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

    def process_item(self, item, spider):
        # self.cursor.execute("insert into mingyan values(item['tag'], item['cont'])")
        # cursor.execute("insert into game values (4,'ppt',1,0,'哈哈')")
        self.cursor.execute(
        """insert into jd(store_names, shop_names, sale_volumes, prices, shop_urls, pic_urls)
        value (%s, %s, %s, %s, %s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
        (item['store_names'],  # item里面定义的字段和表字段对应
         item['shop_names'],
         item['sale_volumes'],
         '￥' + item['prices'],
         'https:' + item['shop_urls'],
         item['pic_urls'],))

        self.connect.commit() # 提交
        return item


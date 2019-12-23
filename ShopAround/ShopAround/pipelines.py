# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
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

    def process_item(self, item, spider):
        # self.cursor.execute(f"""create table {search_name}(
        #                         jd_id int primary key auto_increment,
        #                         store_names varchar(200) default '考拉海购自营',
        #                         prices float(8,2),
        #                         shop_urls varchar(1000),
        #                         pic_urls varchar(1000),
        #                         search_name varchar(20))""")

        for i in range(len(item['prices'])):
            self.cursor.execute(
            """insert into info(shop_names, prices, shop_urls, pic_urls, search_name)
            value (%s, %s, %s, %s, %s)""",
            (
            # item['store_names'][i],
             item['shop_names'][i],
             item['prices'][i],
             item['shop_urls'][i],
             item['pic_urls'][i],
             item['search_name'][i]))
            self.connect.commit() # 提交
        return item


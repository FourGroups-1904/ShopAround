#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/12/14 19:56:51
# @License :   (C) Copyright 2019, {python_1904}




from scrapy import cmdline

cmdline.execute('scrapy crawl jd'.split())
# cmdline.execute(['scrapy', 'rawl', 'jd'])


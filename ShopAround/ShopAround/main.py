#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from scrapy import cmdline
# cmdline.execute('scrapy crawl jd'.split())
# cmdline.execute('scrapy crawl yhd'.split())
# cmdline.execute('scrapy crawl kaolao'.split())
# cmdline.execute(['scrapy', 'rawl', 'jd'])
cmdline.execute('scrapy crawlall'.split())

# print(list(range(1,1)))
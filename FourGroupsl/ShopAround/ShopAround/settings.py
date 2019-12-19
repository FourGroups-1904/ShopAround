# -*- coding: utf-8 -*-

# Scrapy settings for ShopAround project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ShopAround'

SPIDER_MODULES = ['ShopAround.spiders']
NEWSPIDER_MODULE = 'ShopAround.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ShopAround (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {'ShopAround.pipelines.ShoparoundPipeline': 300}  # 500以内 值越小优先级越高

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'en',
    # 'cookie': 'miid=1552569504395725988; cna=uodGFpFSaQUCAWonlmbc3Fza; t=46506dd17e7582bf3a68a99941759e17; lgc=1977681614duoshou; tracknick=1977681614duoshou; _cc_=V32FPkk%2Fhw%3D%3D; tg=0; mt=ci=3_1; thw=cn; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dByuql3%2BnoBzbMhXM%3D&id2=Vy6%2B5h8u0NORDw%3D%3D&nk2=UojTU5CcKKgwWLBbZ%2F8%2Bpdc%3D; uc4=nk4=0%40UOBXUgqrHI8OpqyJ1DT%2F6B5AR7a8MgJxQdNWsg%3D%3D&id4=0%40VXkZxjwJk8WeZ0dlwcJ7LCLk2mhL; enc=3MPd7GnUpBrpXJvBThDHvbNZfmkl2EGM2B7caeD29e93JbRawxrFAbtsyfr%2B%2B3Kj9jqazqrrcOyrF70dNEQZNg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; v=0; cookie2=595e93ad7b1d4b77bfcd9ce65f2ead9c; _tb_token_=3577ed5863e7; _uab_collina=157674070180040116213445; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; x5sec=7b227365617263686170703b32223a22373537383538333765623630343131363233646633613533373839356532663143503363374f3846454b374e6d6f44717a72437671774561444451794e6a63784f4467354e6a49374d513d3d227d; uc1=cookie14=UoTbm8AO7aWnOQ%3D%3D; JSESSIONID=A30B83E5CAA01A40C60A145934AE4168; l=dBEJXwIgqfjtueqLBOCN5uI8Lc7OSIRAguPRwCqvi_5CJ6Ls5gbOkFvSFFp6VjWftkLB4NSLzt29-etkiKy06Pt-g3fPaxDc.; isg=BN_f463B_m0TUPpCxOld-Sa3bjOp7DKdio5SWnEsew7VAP-CeRTDNl3SwtDbmAte'
# }
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ShopAround.middlewares.ShoparoundSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ShopAround.middlewares.ShoparoundDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'ShopAround.pipelines.ShoparoundPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

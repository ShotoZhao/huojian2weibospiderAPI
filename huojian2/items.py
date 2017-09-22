# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Huojian2Item(scrapy.Item):
    title = scrapy.Field()  # 文章标题
    content = scrapy.Field()  # 文章内容
    pubtime = scrapy.Field()  # 发表时间
    readnum = scrapy.Field()  # 阅读人数
    imgurl = scrapy.Field()  # 图片链接

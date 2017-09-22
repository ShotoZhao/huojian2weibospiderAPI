# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json

class Huojian2Pipeline(object):
    def __init__(self):
        self.filename = open("huojian.json", 'a')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False)
        # print (text)
        self.filename.write(text.encode("utf-8")+'\n')
        return item
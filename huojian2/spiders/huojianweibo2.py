# -*- coding: utf-8 -*-
import scrapy
from huojian2.items import Huojian2Item
import re
import json


class Huojianweibo2Spider(scrapy.Spider):
    name = 'huojianweibo2'
    allowed_domains = ['m.weibo.cn','media.weibo.cn']
    url = 'https://m.weibo.cn/api/container/getIndex?uid=5414746957&type=uid&value=5414746957&containerid=1076035414746957&page='
    page = 0
    start_urls = [url+str(page)]

    def parse(self,response):
        urlnext =[]
        key = "article"
        html = response.text
        unicodestr = json.loads(html)
        # print unicodestr
        for feed in unicodestr['cards']:
            if feed.has_key('mblog'):
                if feed['mblog'].has_key('page_info'):
                    urlnext=feed['mblog']["page_info"]['page_url']
                    urlnext = urlnext.split('\n')
                    print urlnext

                    for each in urlnext:
                        print each
                        print "---------------------"
                        if key in each:
                            page_url = each.replace("http","https")
                            yield scrapy.Request(page_url, callback=self.parse_item)

        if self.page<400:
            self.page+=1
        yield scrapy.Request(self.url + str(self.page), callback = self.parse)


    def parse_item(self, response):

        res = response.body.decode('utf-8')
        item = Huojian2Item()

        imgpattern = re.compile('src=(.*?jpg)')
        readnumpat = re.compile(r'"read_count": "(\d+)"')
        pubtimepat = re.compile('"created_at": "(.*)"')
        contentpat = re.compile(r'"content"(.*)')
        titlepat = re.compile('"summary": "(.*?)"')

        # 图片链接
        item['imgurl'] = imgpattern.findall(res)
        # 文章标题
        item['title'] = titlepat.findall(res)
        # 文章内容
        item['content'] = contentpat.findall(res)
        # 发表时间
        item['pubtime'] = pubtimepat.findall(res)
        # 阅读人数
        item['readnum'] = readnumpat.findall(res)

        yield item





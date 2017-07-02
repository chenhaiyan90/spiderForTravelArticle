# -*- coding: utf-8 -*-
import re

import jieba
import scrapy
from scrapy.utils.response import get_base_url

from spiderForChinaCityTravel.items import articleInfoItem


class ChinatravelSpider(scrapy.Spider):
    name = 'chinaTravel'
    allowed_domains = ['travel.china.com.cn']
    start_urls = ['http://travel.china.com.cn/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        activeUrls = []
        for childrenUrl in response.xpath('//a/@href').extract():
            if str(childrenUrl).startswith('txt'):
                fullUrl = response.urljoin(childrenUrl)
                if (fullUrl not in activeUrls):
                    activeUrls.append(fullUrl)
                    self.logger.info(fullUrl)
        for url in activeUrls:
            request = scrapy.Request(url, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        # self.logger.info()
        contentDiv = response.xpath('//div[@class="cp"]').extract_first()
        if contentDiv is None:
             return None
        content = contentDiv.replace('\xa0', '').replace('\r', '').replace('\n', '').replace('\t', '')
        srcs=re.findall(r"src=\"(.*?)\"",content,re.S)
        for a in srcs:
            if a.startswith('http'):
                continue
            content=re.sub(a,response.urljoin(a),content)
        item = articleInfoItem()
        item['originUrl'] = self.start_urls[0]
        item['url'] = get_base_url(response)
        item['originName'] = '旅游中国'
        item['title'] = response.xpath('//title/text()').extract_first().replace('\xa0', ',')
        item['abstracts'] = response.xpath('//meta[@name="description"]').xpath('@content').extract_first()
        keywords = response.xpath('//meta[@name="keywords"]').xpath('@content').extract_first()
        if keywords is None:
            keywords=",".join(jieba._pcut_for_search(item['title']))
        item['keywords'] = keywords
        item['content'] = content
        item['type'] = 'policyNews'
        item['group'] = 'hotspot'
        item['status'] = 'draft'
        item['pageUrls'] = None
        return item

# -*- coding: utf-8 -*-
import jieba
import scrapy
from scrapy.utils.response import get_base_url

from spiderForChinaCityTravel.items import articleInfoItem


class MafengwoSpider(scrapy.Spider):
    name = 'mafengwo'
    allowed_domains = ['www.mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/']
    baseUrl = 'http://www.mafengwo.cn'


    def parse(self, response):
        activeUrls = []
        for childrenUrl in response.xpath('//a/@href').extract():
            if str(childrenUrl).startswith('/i/'):
                fullUrl = response.urljoin(childrenUrl)
                if (fullUrl not in activeUrls):
                    activeUrls.append(fullUrl)
                    self.logger.info(fullUrl)
        # for url in activeUrls:
        #     request = scrapy.Request(url, callback=self.parse_item)
        #     yield request

    def parse_item(self, response):
         # self.logger.info()
        contentDiv = response.xpath('//div[@class="view_con"]').extract_first()
        if contentDiv is None:
             return None
        content = contentDiv.replace('\xa0', '').replace('\r', '').replace('\n', '').replace('\t', '')
        item = articleInfoItem()
        item['originUrl'] = self.baseUrl
        item['url'] = get_base_url(response)
        item['originName'] = '蚂蜂窝'
        item['title'] = response.xpath('//title/text()').extract_first().replace('\xa0', ',')
        item['abstracts'] = response.xpath('//meta[@name="description"]').xpath('@content').extract_first()
        keywords = response.xpath('//meta[@name="keywords"]').xpath('@content').extract_first()
        if keywords is None:
             keywords = ",".join(jieba._pcut_for_search(item['title']))
        item['keywords'] = keywords
        item['content'] = content
        item['type'] = 'travelNote'
        item['group'] = 'hotspot'
        item['status'] = 'draft'
        item['pageUrls'] = None
        return item

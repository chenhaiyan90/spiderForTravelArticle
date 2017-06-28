# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import get_base_url

from spiderForChinaCityTravel.items import articleInfoItem


class TravelpeopleSpider(scrapy.Spider):
    name = 'travelPeople'
    allowed_domains = ['travel.people.com.cn']
    baseUrl = 'http://travel.people.com.cn'

    def start_requests(self):
        start_urls = [
            'http://travel.people.com.cn',
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        activeUrls = []
        for childrenUrl in response.xpath('//a/@href').extract():
            if str(childrenUrl).startswith('/n1'):
                fullUrl = get_base_url(response) + childrenUrl
                if (fullUrl not in activeUrls):
                    activeUrls.append(fullUrl)
                    self.logger.info(fullUrl)
        for url in activeUrls:
            request = scrapy.Request(url, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        # self.logger.info()
        contentDiv = response.xpath('//div[@class="box_con"]').extract_first()
        content = contentDiv.replace('\xa0', '').replace('\r', '').replace('\n', '').replace('\t', '')
        item = articleInfoItem()
        item['originUrl'] = self.baseUrl
        item['url'] = get_base_url(response)
        item['originName'] = '人民旅游网'
        item['title'] = response.xpath('//title/text()').extract_first().replace('\xa0', ',')
        item['abstracts'] = response.xpath('//meta[@name="description"]').xpath('@content').extract_first()
        item['keywords'] = response.xpath('//meta[@name="keywords"]').xpath('@content').extract_first()
        item['content'] = content
        item['type'] = 'policyNews'
        item['group'] = 'hotspot'
        item['status'] = 'draft'
        item['pageUrls'] = None
        return item
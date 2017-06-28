# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from _md5 import md5
from datetime import datetime

import requests

from scrapy.conf import settings

class SpiderforchinacitytravelPipeline(object):
    def process_item(self, item, spider):
        return item
class requestApiStorePipeline(object):
    def __init__(self):
        self.url = settings.get('STORE_URL')
        self.headers = {'Content-Type': 'application/json'}
    def process_item(self, item, spider):
        time=datetime.now().microsecond
        authKey='whahaha'
        authSecret=md5((authKey+str(time-1000)).encode('utf-8')).hexdigest()
        requestData={'time':str(time),'authKey':authKey,'authSecret':authSecret,'md5url':'w2w2d323232323'}
        requestData['url']=item['url']
        requestData['originUrl']=item['originUrl']
        requestData['originName']=item['originName']
        requestData['title']=item['title']
        requestData['keywords']=item['keywords']
        requestData['abstracts']=item['abstracts']
        requestData['content']=item['content']
        requestData['type']=item['type']
        requestData['group']=item['group']
        requestData['status']=item['status']
        requestData['pageUrls']=item['pageUrls']
        response = requests.post(self.url, data=json.dumps(requestData), headers=self.headers)
        print(response.text)
        return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

class BasicEnglishWordsPipeline(object):
    def open_spider(self, spider):
        self.file = open('words.txt', 'w')
    
    def close_spider(self, spider):
        self.file.close()
    
    def process_item(self, item, spider):
        item = dict(item)
        self.file.write(item['word'] + os.linesep)
        return item
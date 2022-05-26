# -*- coding: utf-8 -*-
import re
import scrapy
from basic_english_words.items import BasicEnglishWordsItem


class WordsSpider(scrapy.Spider):
    name = 'words'
    allowed_domains = ['www.usingenglish.com']
    start_urls = ['https://www.usingenglish.com/resources/wordcheck/list-basic+english.html']

    def parse(self, response):
        items = []
        for each in response.xpath("//div[@class='card card-body slimline']"):
            item = BasicEnglishWordsItem()
            word = each.xpath("a/text()").extract()
            word = word[0]
            word = re.sub("[^a-z^A-Z]", "", word) 
            item['word'] = word
            items.append(item)
        return items

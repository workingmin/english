# -*- coding: utf-8 -*-

import bs4
import scrapy
from etymologies_of_words.items import EtymologiesOfWordsItem
from etymologies_of_words.nlp_utils import wordstemmer


class EtymologiesSpider(scrapy.Spider):
    name = 'etymologies'
    allowed_domains = ['www.etymonline.com']
    start_url = "https://www.etymonline.com"

    def __init__(self, words_file=None, *args, **kwargs):
        self.words_file = words_file
        super(EtymologiesSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        if self.words_file is not None:
            with open(self.words_file, 'r') as f:
                for line in f.readlines():
                    word = line.strip()
                    stem = wordstemmer.stem(word)
                    if len(stem) > 0:
                        url = "{}/search?q={}".format(self.start_url, word)
                        item = EtymologiesOfWordsItem()
                        item['word'] = word
                        item['stem'] = stem
                        yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse)

    def parse(self, response):
        url = self.start_url + response.xpath(
            '//div/a[@class="word__name--TTbAA word_thumbnail__name--1khEg"]/@href').extract_first()
        yield scrapy.Request(url=url, meta=response.meta, callback=self.parse_word)

    def parse_word(self, response):
        item = response.meta['item']
        text = '\n'.join(response.xpath('//section[@class="word__defination--2q7ZH"]/p').extract())
        text = bs4.BeautifulSoup(text, features="html.parser").get_text()
        item['text'] = text
        yield item

# -*- coding: utf-8 -*-
import scrapy
from afis_movies.items import AfisMoviesItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['www.afi.com']
    start_urls = ['https://www.afi.com/afis-100-years-100-movies-10th-anniversary-edition/']

    def parse(self, response):
        items = []
        for each in response.xpath('//h6[@class="q_title"]'):
            item = AfisMoviesItem()
            title = each.xpath("text()").extract_first()
            year = each.xpath("span/text()").extract_first().strip('(').strip(')')
            ranking = int(title.split('.', 1)[0].strip())
            name = title.split('.', 1)[1].strip()
            item['name'] = name
            item['ranking'] = ranking
            item['year'] = year
            items.append(item)
        return items

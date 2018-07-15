# -*- coding: utf-8 -*-
import scrapy


class QuanminSpider(scrapy.Spider):
    name = 'quanmin'
    allowed_domains = ['www.quanmin.tv']
    start_urls = ['http://www.quanmin.tv/']

    def parse(self, response):
        pass

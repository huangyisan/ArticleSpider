# -*- coding: utf-8 -*-
import scrapy


class QuanminSpider(scrapy.Spider):
    name = 'quanmin'
    allowed_domains = ['www.quanmin.tv']
    start_urls = ['http://www.quanmin.tv/']

    def parse(self, response):
        anchor_list = response.css("span.common_w-card_host-name::text").extract()
        viewer_list = response.css("span.common_w-card_views-num::text").extract()
        anchor_viewer_dict = dict(zip(anchor_list, viewer_list))
        pass

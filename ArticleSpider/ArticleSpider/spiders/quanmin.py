# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse




class QuanminSpider(scrapy.Spider):
    name = 'quanmin'
    allowed_domains = ['www.quanmin.tv']

    start_urls = ['https://www.quanmin.tv/game/all']



    def parse(self, response):
        next_url = response.css(".list_w-paging_btn.list_w-paging_next::attr(href)").extract_first("")
        if next_url:
            self.parse_detail(response)
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # 单页
        anchor_list = response.css("span.common_w-card_host-name::text").extract()
        viewer_list = response.css("span.common_w-card_views-num::text").extract()
        anchor_viewer_dict = dict(zip(anchor_list, viewer_list))
        sorted(anchor_viewer_dict, key=lambda x:(anchor_viewer_dict.get(x)))
        print(anchor_viewer_dict)



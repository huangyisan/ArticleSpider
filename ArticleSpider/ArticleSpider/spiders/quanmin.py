# -*- coding: utf-8 -*-
import scrapy





class QuanminSpider(scrapy.Spider):
    name = 'quanmin'
    allowed_domains = ['www.quanmin.tv']

    start_urls = []

    def parse(self, response):
        # 单页
        anchor_list = response.css("span.common_w-card_host-name::text").extract()
        viewer_list = response.css("span.common_w-card_views-num::text").extract()
        anchor_viewer_dict = dict(zip(anchor_list, viewer_list))
        pass

    @classmethod
    def get_page_size(cls, response):
        last_page = response.css("div.list_w-videos_paging a::text").extract()[-2].strip()
        return last_page

    @classmethod
    def append_start_urls(cls, page_size):
        start_urls = []
        for i in range(page_size):
            start_urls.append('https://www.quanmin.tv/game/all?p={0}'.format(i))
        return cls.start_urls




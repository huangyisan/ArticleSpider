# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']

    # 爬取需要的url，作为list存放
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        # 加上text()，则直接返回文本信息
        title_xpath = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')
        create_date = create_date.extract()[0].replace('·','').strip()

        # css提取字段
        # ::text 表示以文本的方式输出
        title_css = response.css(".entry-header h1::text").extract()[0]
        pass

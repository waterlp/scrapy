import scrapy


# pip install Scrapy
# scrapy依赖的一些包：
#
# lxml：一种高效的XML和HTML解析器，
# PARSEL：一个HTML / XML数据提取库，基于上面的lxml，
# w3lib：一种处理URL和网页编码多功能辅助
# twisted,：一个异步网络框架
# cryptography and pyOpenSSL，处理各种网络级安全需求


import scrapy
class mingyanSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://lab.scrapyd.cn/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                '内容': quote.css('span.text::text').extract_first(),
                '作者': quote.xpath('span/small/text()').extract_first(),
                '标签': quote.css('.tag::text').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, self.parse)


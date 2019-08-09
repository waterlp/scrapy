import scrapy

class BaiduSpider(scrapy.Spider):

    name = 'baidu'
    # allowed_domains = ['baidu.com']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        print('1111111111111')
        print(response)
        print('1111111111111')
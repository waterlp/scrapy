import scrapy

class My_one(scrapy.Spider):
    name = 'my_one'
    start_urls = 'http://lab.scrapyd.cn/'

    def parse(self, response):
        maincontent =  response.css('div.quote')
        for v in maincontent:
            content = v.css('span.text::text').extract_first() #名言内容
            author = v.css('.author::text').extract_first() #名言内容
            link = v.css('a').extract_first() #名言详情链接
            tag = v.css('.tag::text').extract() #标签
            print(tag)
            tag = ','.join(tag)
            print(tag)


import scrapy
import os

proDir = os.path.split(os.path.realpath(__file__))[0]

class My_one(scrapy.Spider):
    name = 'my_one'
    # start_urls = ['http://lab.scrapyd.cn/']

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self,'tag',None)  # 获取tag值，也就是爬取时传过来的参数
        if tag is not None:     # 判断是否存在tag，若存在，重新构造url
            url = url + 'tag/' + tag  # 构造url若tag=爱情，url= "http://lab.scrapyd.cn/tag/爱情"
        yield scrapy.Request(url, self.parse)  # 发送请求爬取参数内容


    def parse(self, response):
        print('11111111111111111111111')
        maincontent =  response.css('div.quote')
        for v in maincontent:
            content = v.css('span.text::text').extract_first() #名言内容
            author = v.css('.author::text').extract_first() #名言内容
            if author is None:
                author = v.css('small::text').extract_first()  #进入爱情标签页面时获取作者
            link = v.css('a::attr("href")').extract_first() #名言详情链接
            tag = v.css('.tag::text').extract() #标签
            tag = ','.join(tag)

            filename = '%s-语录.txt' % author
            filepath = os.path.join(proDir,"author_content",filename)
            print(filepath)

            with open(filepath,'a+') as f:
                f.write(content)
                f.write('\n')
                f.write("标签：" + tag)
                f.write('\n')
                f.write("链接：" + link)
                f.close()

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)





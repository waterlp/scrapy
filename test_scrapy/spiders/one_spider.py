import scrapy


class One_spider(scrapy.Spider):  # 需要继承scrapy.Spider类


    name = "one_spider"  # 定义蜘蛛名
    start_urls = ['http://lab.scrapyd.cn']
    '''
    start_urls = [  # 另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]
    
    def start_requests(self):  # 由此方法通过下面链接爬取页面

        # 定义爬取的链接
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
        ]
        # response.css('title').extract()[0]
        # response.css('title').extract_first()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # 爬取到的页面如何处理？提交给parse方法处理
    '''

    def parse(self, response):
        '''
        start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        就是这么个流程，似不似很简单呀？


        page = response.url.split("/")[-2]  # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        filename = 'mingyan-%s.html' % page  # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        with open(filename, 'wb') as f:  # python文件操作，不多说了；
            f.write(response.body)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        self.log('保存文件: %s' % filename)  # 打个日志

        '''
        mingyan = response.css('div.quote')  # 提取首页所有名言，保存至变量mingyan

        for v in mingyan:  # 循环获取每一条名言里面的：名言内容、作者、标签

            text = v.css('.text::text').extract_first()  # 提取名言
            autor = v.css('.author::text').extract_first()  # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串

            """
            接下来进行写文件操作，每个名人的名言储存在一个txt文档里面
            """
            fileName = '%s-语录.txt' % autor  # 定义文件名,如：木心-语录.txt

            with open(fileName, "a+") as f:  # 不同人的名言保存在不同的txt文档，“a+”以追加的形式
                f.write(text)
                f.write('\n')  # ‘\n’ 表示换行
                f.write('标签：' + tags)
                f.write('\n-------\n')
                f.close()


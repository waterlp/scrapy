import scrapy

class Shop(scrapy.Spider):
    name = 'shop'
    start_urls = ['http://www.universelife.cn:3000/qyShoppingMall/site/login.html']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'admin', 'password': '111111', 'code':'ee'},
            callback=self.after_login
        )

    def after_login(self, response):
        print(response)
        print(response.text)
        print('111111111111111111111111')
        # check login succeed before going on
        if "欢迎您" in response.body:
            self.logger.error("Login failed")
            return



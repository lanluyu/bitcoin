# -*- coding: utf-8 -*-
import scrapy


class BtcSpider(scrapy.Spider):
    name = 'btc'
    allowed_domains = ['www.8btc.com']
    start_urls = ['http://www.8btc.com/bitcoin']

    def parse(self, response):
        # 先获取每一页中的文章链接
        headers = {
            'Cookie':'UM_distinctid=164253c069b3f-02265862c6ddda-47e1137-100200-164253c069eb7;'
                    +'yd_cookie=8ab1eadd-ec8f-4774a72a9d138e474562faf5866cc57a99cb;'
                    +'CNZZDATA5934906=cnzz_eid%3D1004817248-1529628310-null%26ntime%3D1529720185;'
                    +'QINGCLOUDELB=836e074b593c4f44bd48f6f76fb94554c2f4da300bc4aee30249f3e95199a4b3|Wy3Bl|Wy3Ai',  
            }
        pageurls = response.xpath('.//div[@class="article-title visible-md visible-lg"]/a/@href').extract()
        for pageurl in pageurls:
            print(pageurl)
            yield scrapy.Request(pageurl,callback=self.parse_page,headers=headers)

        # 翻页效果，调用函数本身再进行解析
        for i in range(540):
            basic_url = 'http://www.8btc.com/bitcoin/page/'
            url = basic_url + str(i)
            yield scrapy.Request(url,callback=self.parse)

    def parse_page(self,response):
        # 解析文章页面，获取文章标题和内容
        i = {}
        i['title'] = response.xpath('.//div[@class="article-title"]/h1/text()').extract_first()
        i['article'] = ''.join(response.xpath('.//div[@class="article-content"]//p//text()').extract())
        i['Release_time'] = response.xpath('.//div[@class="single-crumbs clearfix"]/span[3]/time/text()').extract_first()
      
        print(i)
        return i
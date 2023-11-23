# -*- coding: utf-8 -*-
import scrapy
from weather2.items import Weather2Item
from scrapy.http import Request
from scrapy.selector import Selector
import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
base = "E:/weather/"

# 主要思路是：paser->second_paser->detail_parse
##需要注意爬虫脚本的名称和项目重复##

class CountryWeatherSpider(scrapy.Spider):
    name = "CountryWeatherSpider"
    allowed_domains = ['tianqi.com']
    start_urls = ['http://lishi.tianqi.com/']

    # 当我们爬取了大类，然后这时候没有保存item，
    def parse(self, response):
        sel = Selector(response)
        country_urls = sel.xpath('//ul[@class="bcity"]/li[position>1]/a/@href').extract()  # 城市的url
        country_titles = sel.xpath('//ul[@class="bcity"]/li[position>1]/a/text()').extract() # 城市名称

        items = []
        for i in range(0, len(country_titles)):
            file_name = base + country_titles[i]
            # 创建目录
            if (not os.path.exists(file_name)):
                os.makedirs(file_name)
            item = Weather2Item()
            item['country_title'] = country_titles[i]
            item['country_url'] = country_urls[i]
            item['file_name'] = file_name
            items.append(item)
        for item in items:
            # Request的meta功能来传递已经部分获取的item
            yield Request(url=item['country_url'], meta={'item_1': item}, callback=self.second_parse)


    # 对于返回的小类的url，再进行递归请求
    def second_parse(self, response):
        sel = Selector(response)
        item_1 = response.meta['item_1']
        month_urls = sel.xpath('//div[class="tqtongji1"]/ul/li/a/@href').extract()
        month_titles = sel.xpath('//div[class="tqtongji1"]/ul/li/a/text()').extract()

        items = []
        for i in range(0, len(month_urls)):
            item = Weather2Item()
            # second_file_name = item_1['country_title'] + '/' + month_titles[i]
            # if (not os.path.exists(second_file_name)):
            #     os.makedirs(second_file_name)
            item['country_title'] = item_1['country_title']
            item['country_url'] = item_1['country_url']
            item['file_name'] = item_1['file_name']
            item['month_url'] = month_urls[i]
            item['month_title'] = month_titles[i]
            items.append(item)
        for item in items:
            yield Request(url=item['month_url'], meta={'item_2': item}, callback=self.detail_parse)

    def detail_parse(self, response):
        sel = Selector(response)
        item = response.meta['item_2']

        day = sel.xpath('//div[@class="tqtongji2"]/ul[position()>1]/li[1]/a/text()').extract()
        temperate_max = sel.xpath('//div[@class="tqtongji2"]/ul[position()>1]/li[2]/text()').extract()
        temperate_min = sel.xpath('//div[@class="tqtongji2"]/ul[position()>1]/li[3]/text()').extract()
        weather_day = sel.xpath('//div[@class="tqtongji2"]/ul[position()>1]/li[4]/text()').extract()
        wind = sel.xpath('//div[@class="tqtongji2"]/ul[position()>1]/li[5]/text()').extract()
        wind_power = sel.xpath('//div[@class="tqtongji2"]/ul[position()>1]/li[6]/text()').extract()
        item['day'] = day
        item['temperate_max'] = temperate_max
        item['temperate_min'] = temperate_min
        item['weather_day'] = weather_day
        item['wind'] = wind
        item['wind_power'] = wind_power
        yield item


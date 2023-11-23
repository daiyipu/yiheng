# -*- coding: utf-8 -*-
import scrapy
from douban_book.items import DoubanBookItem

class BookSpider(scrapy.Spider):
	"""docstring for BookSpider"""
	name = 'douban_book'
	allowed_domain = ['douban.com']
	start_urls = ['https://book.douban.com/top250']
	
	def parse(self, response):
		yield scrapy.Request(response.url, callback=self.parse_page)

		for page in response.xpath('//div[@class="paginator"]/a'):
			link = page.xpath('@href').extract()[0]
			yield scrapy.Request(link, callback=self.parse_page)

	def parse_page(self, response):
		for item in response.xpath('//tr[@class="item"]'):
			book = DoubanBookItem()
			book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
			book['ratings'] = item.xpath('td[2]/div[2]/span[@class="rating_nums"]/text()').extract()[0]
			book_info = item.xpath('td[2]/p[1]/text()').extract()[0]  
			book_info_contents = book_info.strip().split(" / ")
			book['author'] = book_info_contents[0]   
			book['publisher'] = book_info_contents[-3]   # book_info_contents可能为4段或者5段(包含译者),负索引提取
			book['edition_year'] = book_info_contents[-2]
			book['price'] = book_info_contents[-1]
			yield book
	
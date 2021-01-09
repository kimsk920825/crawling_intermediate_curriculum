import scrapy


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        print(response.url  )

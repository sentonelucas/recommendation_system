import scrapy


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for titles in response.css('h3 a::text'):
            yield{
                'category': response.css('.nav-list ul li::text').get(),
                'stars': response.css('.icon-star::text').get(),
                'price': response.css('.price_color::text').get(),
                'availability': response.css('.availability::text').get()
            } 

import scrapy
from datetime import datetime

class SwigSpider(scrapy.Spider):
    name = "swig80"

    def start_requests(self):

        urls = [
            "https://stooq.pl/q/i/?s=swig80&i",
            "https://stooq.pl/q/i/?s=swig80&l=2&i"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.css('table#fth1 tbody')
        for row in table.css('tr'):
            ticker = row.css('td b font a::text')[0].get()
            name = row.css('td font#f10::text')[0].get()
            price = row.css('td#f13  b span::text')[0].get()
            try:
                book_and_eps = row.css('td#f13::text').getall()
                book_value = book_and_eps[0]
                eps = book_and_eps[1]
            except (IndexError, TypeError):
                book_value, eps = 'null', 'null'
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield {
                'timestamp': timestamp,
                'ticker': ticker,
                'name': name,
                'price': price,
                'book_value': book_value,
                'eps': eps
            }
            

import scrapy

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
        pass

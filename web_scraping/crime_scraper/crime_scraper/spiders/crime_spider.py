import scrapy


class CrimeSpiderSpider(scrapy.Spider):
    name = "crime_spider"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    def parse(self, response):
        pass

import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ["https://www.crimevoice.com/"]

    def parse(self, response):
        for article in response.css("h3 a"):
            yield {"title": article.css("::text").get(), "link": article.attrib["href"]}

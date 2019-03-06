import scrapy

class QuoteSpider(scrapy.Spider):
  name = "hatena"
  

  start_urls = [
    'https://hirocueki.hatenablog.com/',
  ]

  def parse(self, response):
    for quote in response.css('h1.entry-title'):
      yield {
        'title' : quote.css('a::text').get(),
        'url' : quote.css('a::attr(href)').get(),
      }

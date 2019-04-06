import scrapy

class QuoteSpider(scrapy.Spider):
  name = "byomei"


  start_urls = [
    'https://www.qlife.jp/dictionary/search/q_%E5%92%B3/p_1/',
  ]

  def parse(self, response):
    for quote in response.css('h1.entry-title'):
      yield {
        'title' : quote.css('a::text').get(),
        'url' : quote.css('a::attr(href)').get(),
      }

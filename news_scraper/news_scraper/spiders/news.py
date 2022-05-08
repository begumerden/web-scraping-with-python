import json
import logging

from scrapy.spiders import SitemapSpider
from news_scraper.items import NewsArticle


class NewsSpider(SitemapSpider):
  name = 'news'
  allowed_domains = ['www.bbc.com']
  sitemap_urls = ['https://www.bbc.com/sitemaps/https-index-com-news.xml']
  sitemap_rules = [('/turkce', 'parse_article')]

  custom_settings = {
    'FEED_URI': 'results/%(time)s--%(name)s.json'
  }

  def parse_article(self, response):
    logging.info('parse_article function called on %s', response.url)

    article = NewsArticle()

    jsonData = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())
    logging.info(jsonData)

    if jsonData is None:
      return article

    article['url'] = response.url
    article['title'] = jsonData['@graph'][0]['headline']
    article['date'] = jsonData['@graph'][0]['datePublished']
    article['description'] = jsonData['@graph'][0]['description']
    article['text'] = response.xpath('//main[@role="main"]//*//*/text()').get()
    article['source'] = 'BBC'

    return article

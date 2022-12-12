import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DetailFilmSpider(CrawlSpider):
    name = 'detail_film'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    film_details=LinkExtractor(restrict_css = '.titleColumn >a')

    rules_film_details = (
        Rule(film_details, callback='parse_item', follow=False),
    )

    rules = (
        rules_film_details,
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        yield{
            'Titre': response.css(),
        }

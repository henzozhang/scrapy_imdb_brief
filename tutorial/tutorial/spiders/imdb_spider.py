import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        films = response.xpath('//td[@class="titleColumn"]')
        for film in films:
            titre = film.css('a::text').get()
            titre_original = film.css('a::attr(title)').get()
            # titre_original = film.xpath('//a@title').get()
            yield{
            'titre':titre,
            'titre original':titre_original
            }

            #.getall() = .extract()
            #.get() = .extract_first()
# Titre original
# Score
# Genre
# Date
# Durée
# Descriptions(synopsis)
# Acteurs
# Public
# [facultatif] Pays
# [facultatif] Langue d’origine



        

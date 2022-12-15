import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DetailFilmSpider(CrawlSpider):
    name = 'detail_film'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'tutorial.pipelines.TurotialPipeline': 300
    #     }
    #     }

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers={
            'User-Agent': self.user_agent
        })

    film_details=LinkExtractor(restrict_css='.titleColumn >a')

    rules_film_details = (
        Rule(film_details, callback='parse_item', follow=False)
    )

    rules = (
        rules_film_details,
    )

    def parse_item(self, response):
        
        duree =response.xpath('//li[@class="ipc-inline-list__item"]/text()').getall()
        la_duree = int(duree[0])*60+int(duree[3])
      
        yield{
            'Titre original': response.css('h1::text').get(),
            'Score sur 10' : response.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()').get(),
            'Genre':response.xpath('//span[@class="ipc-chip__text"]/text()').get(),
            'Date de sorti en USA' : response.xpath('//a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"]/text()').get(),
            'Descriptions' : response.xpath('//span[@class="sc-16ede01-2 gXUyNh"]/text()').get(),
            'Duree' : la_duree,
            'Acteurs': response.xpath('//a[@class="sc-bfec09a1-1 gfeYgX"]/text()').extract(),
            'Public' : response.xpath('//a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"]/text()').get(),
            "Pays d’origine" : response.xpath('/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section/div[2]/ul/li[2]/div/ul/li/a/text()')[0].extract(),
            #"langue d’origine": response.xpath('/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section/div[2]/ul/li[4]/div/ul/li/a/text()')[1].extract()
            
        }
            
        







import scrapy
from crawling.items import ParliamentMembersItem


class ParliamentSpider(scrapy.Spider):
    name = 'parliament'
    allowed_domains = ['parliament.bg']
    start_urls = ['https://www.parliament.bg/bg/MP/']

    def parse(self, response):
        parliament_urls = response.css('div.MPinfo a::attr(href)').extract()
        for url in parliament_urls:
            link = 'https://www.parliament.bg' + url + '/'
            yield scrapy.Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        items = ParliamentMembersItem()

        items['name'] = response.css('div.MPBlock_columns2 img::attr(alt)').get(default='')

        for i in range(1, len(response.css('div.MPinfo ul.frontList > li')) + 1):
            response_text = response.css('ul.frontList > li:nth-child({})::text'.format(i)).get(default='')
            if 'Дата на раждане' in response_text:
                items['date_birth'] = response_text
                items['place_birth'] = response_text
            elif 'Професия' in response_text:
                items['profession'] = response_text
            elif 'Избран(а)' in response_text:
                items['selected_with'] = response_text
            elif 'E-mail' in response_text:
                items['email'] = response.css('ul.frontList > li:nth-child({}) a::text'.format(i)).get(default='')
            elif 'Езици' in response_text:
                items['languages'] = response_text
        
        items['image'] = response.css('div.MPBlock_columns2 img::attr(src)').get(default='')

        yield items

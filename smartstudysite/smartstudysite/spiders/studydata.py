import scrapy
from ..items import SmartstudysiteItem

class DatasSpider(scrapy.Spider):
    name = 'data'
    start_urls = [
        'https://www.geeksforgeeks.org/python'


    ]

    def parse(self,response,**kwargs):
        items = SmartstudysiteItem()

        all_div_data = response.css('div.entry-content')

        for data in all_div_data:

            topic = data.css('h1::text').extract()

            content = data.css('p::text').extract()

            items['topic'] = topic

            items['content'] = content


            yield items

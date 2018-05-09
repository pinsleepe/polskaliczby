from scrapy import Spider
from scrapy.selector import Selector

from polskaliczby.items import StackItem


class WojSpider(Spider):
    name = "woj"
    allowed_domains = ["www.polskawliczbach.pl"]
    start_urls = [
        "http://www.polskawliczbach.pl",
    ]

# 'a[@class="question-hyperlink"]/text()'
# /* means “any element under the root node”
# shortcut when you do not know at what level you expect your target node to be //body//p
# @ prefix before the attribute name

    def parse(self, response):


        # questions = Selector(response).xpath('//*[@id="lstTab"]/tbody/tr')
        #
        # for question in questions:
        #     item = StackItem()
        #     item['Wojewodztwo'] = question.xpath('td[2]/a/@href').extract()[0]
        #     item['Populacja'] = question.xpath('td[3]/text()').extract()[0]
        #     item['Obszar'] = question.xpath('td[4]/text()').extract()[0]
        #     item['Stopa_urbanizacji'] = question.xpath('td[5]/text()').extract()[0]
        #     yield item


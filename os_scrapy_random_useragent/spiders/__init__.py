# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from os_scrapy_random_useragent.items import ExampleItem


class ExampleSpider(scrapy.Spider):
    """ ExampleSpider
    Auto generated by os-scrapy-cookiecuter

    Run:
        scrapy crawl example
    """

    name = "example"

    start_urls = ["http://example.com/"]

    def parse(self, response):
        yield ExampleItem(
            url=response.url,
            request_headers=response.request.headers,
            response_headers=response.headers,
            status=response.status,
            meta=response.meta,
            body=response.body,
        )

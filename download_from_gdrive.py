"""A Scrapy-based gdrive downloader ignoring the large file warning"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request

class GoogleDriveSpider(scrapy.Spider):
    """Small spider for downloading large files from gdrive"""
    name = 'Google Drive Large File Downloader'
    start_urls = ['https://drive.google.com/uc?id=1IOh3HWQAU2kcdpyPxWfNaNAnwCaUKv2P']

    def parse(self, response):
        """Parses Google's warning page."""
        downlaod_url = 'https://drive.google.com' + \
            response.xpath('//div[@class="uc-main"]'
                           + '/div[@id="uc-text"]/a/@href').extract()[0]
        yield Request(url=downlaod_url, callback=self.save_file,
                      meta={'download_maxsize' : 0})

    def save_file(self, response):
        """Saves downloaded file."""
        name = 'CARLA_0.7.1.tar.gz'
        with open(name, 'wb') as large_file:
            large_file.write(response.body)


if __name__ == "__main__":
    spiderproc = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    spiderproc.crawl(GoogleDriveSpider)
    spiderproc.start()

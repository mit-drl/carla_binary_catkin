"""A Scrapy-based gdrive downloader ignoring the large file warning"""
from __future__ import print_function
import logging
import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request


class GoogleDriveSpider(scrapy.Spider):
    """Small spider for downloading large files from gdrive"""
    name = 'Google Drive Large File Downloader'


    def __init__(self, url, file_name):
        self.file_name = file_name
        self.start_urls = [url]

    def parse(self, response):
        """Parses Google's warning page."""
        downlaod_url = 'https://drive.google.com' + \
            response.xpath('//div[@class="uc-main"]'
                           + '/div[@id="uc-text"]/a/@href').extract()[0]
        yield Request(url=downlaod_url, callback=self.save_file,
                      meta={'download_maxsize' : 0})

    def save_file(self, response):
        """Saves downloaded file."""
        with open(self.file_name, 'wb') as large_file:
            large_file.write(response.body)


if __name__ == "__main__":
    # Reduce Scrapy logger verbosity.
    logging.disable(logging.WARNING)
    spiderproc = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    spiderproc.crawl(GoogleDriveSpider, url=sys.argv[1], file_name=sys.argv[2])
    spiderproc.start()

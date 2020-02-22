import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrape_songs.spiders.album_spider


def run(args):
    process = CrawlerProcess(get_project_settings())


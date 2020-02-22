import scrapy
from scrapy.crawler import CrawlerProcess
from os import remove

from scrape_songs.spiders.album_spider import AlbumSpider


def run(args=None):
    remove("albums.jl")
    process = CrawlerProcess(settings={
        "FEED_FORMAT": "jl",
        "FEED_URI": "albums.jl"
    })

    process.crawl(AlbumSpider)
    process.start()


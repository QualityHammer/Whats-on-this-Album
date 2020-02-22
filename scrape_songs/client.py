import scrapy
from scrapy.crawler import CrawlerProcess
from os import remove

from scrape_songs.spiders.album_spider import AlbumSpider
from scrape_songs.search_wiki import get_album_info


def run(args=None):
    remove('albums.jl')
    process = CrawlerProcess(settings={
        "FEED_FORMAT": "jl",
        "FEED_URI": "albums.jl",
        "COOKIES_ENABLED": False
    })

    album_info = get_album_info(args.album_names)

    process.crawl(AlbumSpider, album_info['urls'])
    process.start()


class test:
    album_names = [
        "lynyrd skynyrd Street Survivors",
        "kendrick section 80"
    ]


if __name__ == "__main__":
    run(test())


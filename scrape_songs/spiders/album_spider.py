import scrapy


class AlbumSpider(scrapy.Spider):
    name = "albums"

    def __init__(self, album_urls, *args, **kwargs):
        super(AlbumSpider, self).__init__(*args, **kwargs)
        self.start_urls = album_urls

    def parse(self, response):
        song_names = []
        for row in response.css('table.tracklist')[0].css('tr')[1:]:
            song_names.append(
                    row.css('td::text')[1].get()
                    .replace("\\", '').replace("\"", ''))

        yield {
            "song_names": song_names
        }


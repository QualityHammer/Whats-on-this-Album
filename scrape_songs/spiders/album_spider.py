import scrapy


class AlbumSpider(scrapy.Spider):
    name = "albums"
    start_urls = [
        'https://en.wikipedia.org/wiki/Step_in_the_Arena_(album)',
        'https://en.wikipedia.org/wiki/Unlocked_(EP)'
    ]

    def parse(self, response):
        song_names = []
        for row in response.css('table.tracklist')[0].css('tr')[1:]:
            song_names.append(
                    row.css('td::text')[1].get()
                    .replace("\\", '').replace("\"", ''))

        yield {
            "song_names": song_names
        }


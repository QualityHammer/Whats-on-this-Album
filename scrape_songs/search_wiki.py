from wikipedia import seacrh, page


def get_album_title(album_name):
    return search(album_name, results=1)[0]


def get_album_url(album_title):
    return page(album_title).url


def get_album_info(album_name_list):
    album_titles = []
    album_urls = []
    for album_name in album_name_list:
        title = get_album_title(album_name)
        url = get_album_url(title)
        album_titles.append(title)
        album_urls.append(url)

    return {
        "titles": album_titles,
        "urls": album_urls
    }


def check_for_title(table):
    try:
        return "title" in table.css('td::text')[1] \
                .get().lower()
    except IndexError:
        return False


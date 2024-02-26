from lxml import html

class LastFiveBoxScore:
    def __init__(self, html):
        self.html = html
        self._BASE_URL = "https://www.basketball-reference.com/players/{}/{}}.html"
        self._xpath = '//div[@class="table_container"]//tbody/tr/td[@data-stat="{}"]'

    @property
    def date(self):
        row = self.html.xpath(self._xpath.format("date"))

        if len(row) > 0:
            return row[0].text_content()

        return ''
    
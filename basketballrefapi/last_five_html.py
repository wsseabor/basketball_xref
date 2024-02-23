from lxml import html

class LastFiveBoxScore:
    def __init__(self, html):
        self.html = html

    @property
    def date(self):
        row = self.html.xpath('td[@data-stat="date"]')

        if len(row) > 0:
            return row[0].text_content()

        return ''
    
    @property
    def team_abbreviation(self):
        row = self.html.xpath('td[@data-stat="team_name_abbr"]')

        if len(row) > 0:
            return row[0].text_content()
        
        return ''
    
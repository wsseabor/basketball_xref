import requests
from lxml import html
from lxml import etree

url = "https://www.basketball-reference.com/players/a/antetgi01.html"

re = requests.get(url)

rows = []

tree = html.fromstring(re.content)

headers = tree.xpath('//div[@class="table_container"]//thead')
#ex = tree.xpath('//div[@class="table_container"]//tbody/tr[not(contains(@class, "thead"))]')

#ex = tree.xpath('//div[@class="table_container"]//tbody/tr/td[@data-stat="mp"]')

"""
for row in ex:
    print(row.text_content())
"""

"""
for row in headers:
    print(row.text_content())
"""

def split_rows():

    query = '//div[@class="table_container"]//tbody/tr/td[@data-stat="{}"]'

    paths = []

    keys = [
        "date",
        "team_name_abbr",
        "game_location",
        "opp_name_abbr",
        "game_result",
        "is_starter",
        "mp",
        "fg",
        "fga",
        "fg_pct",
        "fg3",
        "fg3a",
        "fg3_pct",
        "ft",
        "fta",
        "ft_pct",
        "orb",
        "drb",
        "trb",
        "ast",
        "stl",
        "blk",
        "tov",
        "pf",
        "pts",
        "game_score",
        "plus_minus"
    ]

    for i in keys:
        paths.append(query.format(i))

    return paths

queries = split_rows()
results = []

for i in queries:
    stat = tree.xpath(i)

    for row in stat:
        print(row.text_content())

for row in stat:
    print(row.text_content())








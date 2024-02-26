import requests
from lxml import html
from lxml import etree
import csv

url = "https://www.basketball-reference.com/players/a/antetgi01.html"

re = requests.get(url)

rows = []

tree = html.fromstring(re.content)

headers = tree.xpath('//div[@class="table_container"]//thead')
#ex = tree.xpath('//div[@class="table_container"]//tbody/tr[not(contains(@class, "thead"))]')

#ex = tree.xpath('//div[@class="table_container"]//tbody/tr/td[@data-stat="mp"]')

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
header_rows = [
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

stats_rows = []

for i in queries:
    stat = tree.xpath(i)
    
    for row in stat:
        stats_rows.append(row.text_content())

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header_rows)

    writer.writerow(stats_rows)





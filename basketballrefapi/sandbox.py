import requests
from lxml import html

url = "https://www.basketball-reference.com/players/a/antetgi01.html"

re = requests.get(url)

tree = html.fromstring(re.content)

headers = tree.xpath('//div[@class="table_container"]//thead')
ex = tree.xpath('//div[@class="table_container"]//tbody/tr[not(contains(@class, "thead"))]')

for row in ex:
    print(row.text_content())

for row in headers:
    print(row.text_content())

def split_rows(page):
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
        "fg3a"
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
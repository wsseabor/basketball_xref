"""

Please don't look at this

"""

import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
import csv
import pandas as pd

"""

-- LXML example that is tough to operate -- 

url = "https://www.basketball-reference.com/players/a/antetgi01.html"

re = requests.get(url)

rows = []

tree = html.fromstring(re.content)

headers = tree.xpath('//div[@class="table_container"]//thead')
ex = tree.xpath('//div[@class="table_container"]//tbody/tr[not(contains(@class, "thead"))]')

ex = tree.xpath('//div[@class="table_container"]//tbody/tr/td[@data-stat="mp"]')


def split_rows():

    query = '//div[@class="table_container"]//tbody/tr/td[@data-stat="{}"]/text()'

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
        stats_rows.append(row)

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header_rows)

    for row in range(len(header_rows)):
        writer.writerow(stats_rows[row])
"""

"""

-- Beautiful soup example transforming into pandas dataframe

"""

url = "https://www.basketball-reference.com/players/a/antetgi01.html"

re = requests.get(url)

soup = BeautifulSoup(re.text, 'lxml')

table_data = soup.find('table', { 'class' : 'sortable stats_table' })

def get_headers(page):
    page = soup.find('table', { 'class' : 'sortable stats_table'})

    headers = page.find_all('th', scope = 'col')

    return [td.get_text(strip = True) for td in headers]

def get_table_data(page):
    page = soup.find('table', attrs = { 'class' : 'sortable stats_table'})

    stats = page.find_all(['th', 'td'], attrs = { 'data-stat' : any})

    return [td.get_text(strip = True) for td in stats][len(headers):]

def table_data_text(table):

    def row_get_data_text(tr, coltag='td'):    
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]

    rows = []
    trs = table.find_all('tr')
    header_row = row_get_data_text(trs[0], 'th')

    if header_row:
        rows.append(header_row)
        trs = trs[1:]

    for tr in trs:
        rows.append(row_get_data_text(tr, 'td'))

    return rows

headers = get_headers(re)
data = get_table_data(re)

print(headers)
print(data)

"""
list_table = table_data_text(table_data)
print(list_table[:5])

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(list_table[0])
    writer.writerows(list_table[1:])

df = pd.DataFrame(list_table[1:], columns = list_table[0])
df.head(5)
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv


"""

   Beautiful soup scraping for last five games on basketball reference, transforming data 
   into JSON format, output to csv file, small test case for later expansion
 

"""

#Example URL for a player
url = "https://www.basketball-reference.com/players/a/antetgi01.html"

#Requests library to get page information
re = requests.get(url)

#Beautiful soup constructor
soup = BeautifulSoup(re.text, 'lxml')

#Get last five games page headers, @param page to be scraped, returns list of headers
def get_headers(page):
    page = soup.find('table', { 'class' : 'sortable stats_table'})

    headers = page.find_all('th', scope = 'col')

    return [td.get_text(strip = True) for td in headers]

#Get last five games table data, @param page to be scraped, returns list of table data
def get_table_data(page):
    page = soup.find('table', attrs = { 'class' : 'sortable stats_table'})

    stats = page.find_all(['th', 'td'], attrs = { 'data-stat' : any})

    return [td.get_text(strip = True) for td in stats][len(headers):]

#Call methods to create headers and data
headers = get_headers(re)
data = get_table_data(re)

#Converts headers and table data to list of list of dictionaries
def to_dict(keyList, valueList):

    out = []

    for i in range(int(len(valueList) / len(keyList))):
        out += [dict(zip(keyList, valueList[i: i + len(keyList)]))]
    
    return out

#Convert to JSON notation
x = to_dict(headers, data)
final = json.dumps(x, indent = 2)

#Convert to csv
with open('test.csv', 'w') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    writer.writerows(x)

#Convert to csv with pandas
"""
df = pd.DataFrame(x)
df.to_csv('test.csv')
"""

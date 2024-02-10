#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

"""
url = "https://www.basketball-reference.com/players/s/sharpsh01.html"

html = urlopen(url)

soup = BeautifulSoup(html, features="html.parser")

last_five_table = soup.find(id="div_last5")

pd_last_five = pd.read_html(str(last_five_table))
"""

def player_name_format(fname, lname):
    formatted_l_name = lname[:5]
    formatted_f_name = fname[:2]


    return f"{formatted_l_name}{formatted_f_name}01".lower()

def get_player_lname_initial(formatted_name):
    return formatted_name[0]
    

def convert_player_name_to_url(initial, formatted_name):
    return f"https://www.basketball-reference.com/players/{initial}/{formatted_name}.html"

formatted_player_name = player_name_format("Demar", "Derozan")
player_initial = get_player_lname_initial(formatted_player_name)
test = convert_player_name_to_url(player_initial, formatted_player_name)

url = test

response = requests.get(url)
response_text = response.text
print(response.status_code)

df = pd.read_html(response_text, attrs={'id' : 'last5'})

df
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

from data import Location, Outcome, TEAM_ABBREVIATIONS_TO_TEAM

def parse_location(symbol):
    if symbol == "@":
        return Location.AWAY
    elif symbol == "":
        return Location.HOME
    raise ValueError(f"Unable to parse {symbol}.")

def parse_outcome(symbol):
    if symbol == "W":
        return Outcome.WIN
    elif symbol == "L":
        return Outcome.LOSS
    raise ValueError(f"Unable to parse {symbol}.")

def parse_player_last_five(row):
    return {
        
    }
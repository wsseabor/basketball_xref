from lxml import html

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

def parse_games_started(symbol):
    if symbol == "*":
        return symbol
    else:
        raise ValueError(f"Unable to parse {symbol}.")

def parse_player_last_five(row):
    return {
        "date": str(row[1].text_content()),
        "team": TEAM_ABBREVIATIONS_TO_TEAM[row[2].text_content()],
        "location": parse_location(row[3].text_content()),
        "opponent": TEAM_ABBREVIATIONS_TO_TEAM[row[4].text_content()],
        "outcome": parse_outcome(row[5].text_content()),
        "games_started": parse_games_started(row[6].text_content()),
        "minutes_played": int(row[7].text_content()),
        "field_goals": int(row[8].text_content()),
        "field_goal_attempts": int(row[9].text_content()),
        "field_goal_percentage": float(row[10].text_content()),
        "three_points": int(row[11]).text_content(),
        "three_point_percentage": float(row[12].text_content()),
        "free_throws": int(row[13].text_content()),
        "free_throw_attempts": int(row(14).text_content()),
        "free_throw_percentage": float(row[15].text_content()),
        "offensive_rebounds": int(row[16].text_content()),
        "defensive_rebounds": int(row[17].text_content()),
        "total_rebounds": int(row[18].text_content()),
        "assists": int(row[19].text_content()),
        "steals": int(row[20].text_content()),
        "blocks": int(row[21].text_content()),
        "turnovers": int(row[22].text_content()),
        "personal_fouls": int(row[23].text_content()),
        "points": int(row[24].text_content()),
        "game_score": float(row[25].text_content()),
        "plus_minus": float(row[26].text_content()),
    }

def parse_player_last_five(page):
    tree = html.fromstring(page)
    rows = tree.xpath('//table[@id="last5"]')
    return list(map(lambda row: parse_player_last_five(row), rows))

#Unsure
#//tbody/tr[not(contains(@class, "thead"))]




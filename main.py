import requests
import pandas as pd
from bs4 import BeautifulSoup

# This contains the subheadings of the webpages that we want to access
web_links = ['shooting', 'passing', 'passing_types', 'gca', 'defense', 'possession']
dataframe = pd.DataFrame
headers = []
details_header = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s']

def get_web_req(url_req):
    url = 'https://fbref.com/en/comps/Big5/' + url_req + '/players/Big-5-European-Leagues-Stats'

    page = requests.get(url).text

    # Creating BeautifulSoup object
    soup = BeautifulSoup(page, 'html.parser')

    return soup


"""
Get the player information
"""

soup = get_web_req("shooting")
dataframe = pd.DataFrame(columns=details_header)
for table in soup.find_all(id="stats_shooting"):
    for row in (soup.find_all("tr")):
        player = []
        count = 0
        for item in row.find_all("td"):
            if count < len(details_header):
                player.append(item.text)
            count += 1


        if len(player) == len(details_header):
            dataframe = dataframe.append(pd.DataFrame([player], columns=details_header), ignore_index=True)


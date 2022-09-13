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

for i in range(0, len(web_links)):

    this_headers = []

    soup = get_web_req(web_links[i])

    for headers in soup.find_all("th", {'class' : ['poptip center', 'poptip center group_start', 'poptip hide_non_quals center']}):
        if headers.text == 'Matches':
            break
        if headers.text not in details_header and headers.text != '' and headers.text != 'Standard' \
                and headers.text != 'Expected':
            this_headers.append(headers['aria-label'])
    df = pd.DataFrame(columns=this_headers)

    for table in soup.find_all(id="stats_" + web_links[i]):

        for row in (soup.find_all("tr")):
            player = []
            counter = 0
            for item in row.find_all("td"):
                if counter > len(details_header) - 2 and item.text != 'Matches':
                    if item.text == '':
                        app = 0
                    else:
                        app = float(item.text)
                    player.append(app)
                counter += 1

            if len(player) == len(this_headers):
                df = df.append(pd.DataFrame([player], columns=this_headers), ignore_index=True)
    dataframe = df if dataframe.empty else pd.concat([dataframe, df], axis=1)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

dataframe.to_excel("test.xlsx")

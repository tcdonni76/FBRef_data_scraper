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
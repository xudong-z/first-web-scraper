
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# This is a list of Academy Award–winning films.
# This list contains many films that won Academy Awards, up to February 2017.
url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"

# below is the code that scrape the main table.
# finally it will cache a longlist of film information (length = 170)
# and each element of the longlist is a shortlist that contains information of film name, year, awards, nominations

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
main_table = soup.find('table',{'class':"wikitable sortable"})

header = ["film","year", "awards", "nominations","awards_ratio"]
info_list = [header,]
# parsing the main_table
for info in main_table.select('tr'):
    if info.get_text().strip().split('\n')[0] != "Film": # to avoid the header
        film_info = info.get_text().strip().split('\n') # to get a list of film name, year, awards, nominations
        if film_info[2] != '2' and film_info[2] != '1':   # only scrape films that won more than 2 awards at a time
            if not film_info[3].endswith(']') and not film_info[2].startswith('0') and not film_info[2].endswith(')') : # to do more cleaning
                awards_ratio = round(int(film_info[2])/int(film_info[3]),3)
                film_info.append(awards_ratio)
                info_list.append(film_info)

source1 = pd.DataFrame(info_list)
source1.to_csv("local_data/pre_local_source1.csv" ,header = False)

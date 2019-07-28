## source 1
## to get the info_list of films that won more than 1 academy awards_list (170 in all history)
## source 1 will also be the source for source 2 & 3
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"

def source1(number):
    # below is the code that scrape the main table
    print("**Now loading source1!**")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    main_table = soup.find('table',{'class':"wikitable sortable"})
    header = ["film","year", "awards", "nominations","awards_ratio"]
    info_list = [header]

    for info in main_table.select('tr'):
        if info.get_text().strip().split('\n')[0] != "Film": # to avoid the header
            film_info = info.get_text().strip().split('\n') # to get a list of film name, year, awards, nominations
            if film_info[2] != '2' and  film_info[2] != '1' :   # only scrape films that won more than 2 awards at a time
                if not film_info[3].endswith(']') and not film_info[2].startswith('0') and not film_info[2].endswith(')') : # to do more cleaning
                    awards_ratio = round(int(film_info[2])/int(film_info[3]),3)
                    film_info.append(awards_ratio)
                    info_list.append(film_info)
    # In this way, we get a list of Academy Award–winning films.
    # This list contains 170 films that won more than 2 Academy Awards, up to February 2017.

    # extract the input number of records
    source1 = pd.DataFrame(info_list[:int(number)+1])
    # save it to local disk to make it safe
    source1.to_csv("remote_data/remote_source1.csv", header = False)

    print("-- Source1 info loaded")
    print("**Thanks for using source1!**\n")

    return source1

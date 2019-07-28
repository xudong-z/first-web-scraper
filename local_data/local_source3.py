## source 3
## besed on the long info_list generated in driver file,
## I will use the film names to scrape the latest and most relevant news tiles and its link

import requests
import json
import pandas as pd

source1 = pd.read_csv("local_source1.csv")

header = ["film", "news_title", "news_link"]
source3 = [header]
# the API for all news websites
# it will return all the news that are within 5 days and related to this film name (sorted by relavancy)
# for grader: this API is a bit slow (about 3 seconds for one record)
endpoint2 = 'http://webhose.io/filterWebContent?token=a8b810b8-88f0-4385-af42-9f1d6863d01d&format=json&sort=relevancy&q={}%20is_first%3Atrue%20site_type%3Anews'

#def source3(number, info_list):

source1 = pd.read_csv("source1.csv")

# to get all the names from the pd.df
for film in source1.film:
    # attach a "film" to every film name is to improve the relavancy
    # imagine different response to "moonlight" and "moonlight film movie"
    film2 = film + " film"
    formatted_film2 = "%20".join(film2.split(" "))   # format the film title into url
    film_url2 = endpoint2.format(formatted_film2)
    # request the film_json2
    try:
        film_response2 = requests.get(film_url2)
        film_json2 = json.loads(film_response2.text)
        # parsing the film_json2
        news_title = film_json2['posts'][0]['title']
        news_link = film_json2['posts'][0]['url']

        film_info = [film, news_title, news_link]
        print(film_info)

    except:
        film_info = [film, "NA", "NA"]
        print(film.encode('utf-8') , " is not found!\n")

    source3.append(film_info)

source3 = pd.DataFrame(source3)
source3.to_csv("local_source3.csv", header = False)

print("\n***Thanks for using Source 3!***\n")

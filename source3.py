## source 3
## will use the film names to scrape the latest and most relevant news tiles and its link
import requests
import json
import pandas as pd

# the API for all news websites
# it will return all the news that are within 5 days and related to this film name (sorted by relavancy)
# for grader: this API is a bit slow (about 3 seconds for one record)
endpoint2 = "http://webhose.io/filterWebContent?token=00eae0cd-286a-445e-a18d-6f02d010f4f3&format=json&sort=relevancy&q=language%3Aenglish%20t"

def source3():
    print("**Now loading source3!**")
    # continue to explore the selected films
    source1 = pd.read_csv("remote_data/remote_source1.csv")
    # extract film titles for API
    film_list = source1.film
    news_title_list = []
    news_link_list = []

    for film in film_list:
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
            # finaly, we can get two lists of titles and links of the most relevant news
            news_title_list.append(news_title)
            news_link_list.append(news_link)
            print("-- Source3 API info is added for %s" %(film))

        except:
            # to avoid any missing values
            news_title_list.append("N/A")
            news_link_list.append("N/A")
            print("-- Source3 API info is not available for %s" %(film))

    # save the data into a pd.DataFrame and local .csv file
    source3 = {"film":film_list, "news_title": news_title_list, "news_link":news_link_list}
    source3 = pd.DataFrame(data = source3)
    source3.to_csv("remote_data/remote_source3.csv", header = True)

    print("**Thanks for using Source3!**\n")

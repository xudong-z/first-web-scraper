## source 2
## besed on the long info_list generated in source1 file,
## I will use the film names to scrape the corresponding box-office revenue
import requests
import json
import pandas as pd

# the API for imdb data base
endpoint1 = 'http://www.omdbapi.com/?apikey=7e7783f5&t='

def getNumber(string):
    # the extracted data might be "$1,234,567", and this is to clean it into integer "1234567"
    remove_dollar = string.split("$")[1]
    remove_comma = "".join(remove_dollar.split(","))
    number = int(remove_comma)
    return number

def source2():
    # continue to explore the selected films
    print("**Now loading source2!**")
    source1 = pd.read_csv("remote_data/remote_source1.csv")
    # extract film titles for API
    film_list = source1.film
    boxoffice_list = []

    for film in film_list:
        try:
            formatted_film = "+".join(film.split(" ")) # format the film title into url
            film_url = endpoint1 + formatted_film  # beacuse both upper case and lower case work, so simply connect the string
            film_response = requests.get(film_url) # request the film_json
            film_json = json.loads(film_response.text)
            boxoffice = film_json["BoxOffice"] # parsing the film_json and get the boxoffice info
            boxoffice_list.append(boxoffice) # to save into a list and then a pd.df
            print("-- Source2 API info added for %s" %(film))

        except:
            # to avoid any missing values
            boxoffice_list.append("N/A")
            print("-- Source2 API info is not available for %s" %(film))

    # save the data into a pd.DataFrame and local .csv file
    source2 = {"film":film_list, "boxoffice": boxoffice_list}
    source2 = pd.DataFrame(data = source2)
    source2.to_csv("remote_data/remote_source2.csv", header = True)
    print("**Thanks for using Source2!**\n")
    return source2

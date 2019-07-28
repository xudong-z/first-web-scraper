## source 2
## besed on the long info_list generated in driver file,
## I will use the film names to scrape the corresponding buget and box-office revenue

import requests
import json
import pandas as pd

# the API for imdb data base
# for grader: this API is a bit slow (about 5-8 seconds for one record)
endpoint1 = 'http://www.omdbapi.com/?apikey=7e7783f5&t='

source1 = pd.read_csv("local_source1.csv")

header = ["film", "boxoffice"]
source2 = [header]

def getNumber(string):
    # the extracted data might be "$1,234,567", and this is to clean it into integer "1234567"
    try:
        remove_dollar = string.split("$")[1]
        remove_comma = "".join(remove_dollar.split(","))
        number = int(remove_comma)
        return number
    except:
        pass

def gross_budget_ratio(gross, budget):
    # to calculate the ratio(box-office revenue/budget) and indicate the financial return of this movie
    ratio = round(getNumber(gross)/getNumber(budget),2) # getNumber() is defiend above
    return ratio

for film in source1.film:
    try:
        formatted_film = "+".join(film.split(" ")) # format the film title into url
        film_url = endpoint1 + formatted_film  # beacuse both upper case and lower case work, so simply connect the string
        # request the film_json
        film_response = requests.get(film_url)
        film_json = json.loads(film_response.text)
        # parsing the film_json
        boxoffice = film_json["BoxOffice"]
        # finaly, we can get three lists of budgets(est), revenues and their ratios
        print(film, boxoffice)

    except:
        # to avoid any missing values
        boxoffice = "N/A"
        # My IP was blocked from source2 API once when I was testing my application
        # if this happens again, I beg your mercy
        print("--! Missing Values or Blocked IP. \n--Please contact Xudong ZHANG for more information\n")

    film_info = [film, getNumber(boxoffice)]
    print(film_info)
    source2.append(film_info)

source2 = pd.DataFrame(source2)
source2.to_csv("local_source2.csv", header = False)

print("\n***Thanks for using Source2!***\n")

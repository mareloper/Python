##This file will be handling everything about requests as a library
import requests

countries_url = "https://restcountries.eu/rest/v2/all"

##getting the data from the declared url
countries = requests.get(countries_url)

##printing the data
print(countries)

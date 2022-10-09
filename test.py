from archive import key
import json
import requests


API_KEY = key

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def Url(city):

    #Builds the URL and shoots it into browser thanks to the requests module
    URL = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(URL)
    weather_info = response.json
    data = response.content

    #Saves the data as a Json file
    with open("data.json", "wb") as f:
        f.write(data)


    #opens the Json file for data extraction by converting the json into a dictionary
    file = open("data.json", "r")
    json_data = json.load(file)

    print(type(json_data))

    #this code displays all the data at once
    #for key, value in json_data.items():
    #    print(f"\n key: {key}")
    #    print(f"Data: {value} \n")

    print(json_data["name"])
    print(json_data["main"])


    file.close()




city = input("enter the city name you want to search up on?:  ")

Url(city)
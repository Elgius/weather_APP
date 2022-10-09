from archive import key
import json
import requests


API_KEY = key

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def Url(city):

    #URL = f"{BASE_URL}?q={city}&appid={API_KEY}"
    #response = requests.get(URL)
    #weather_info = response.json
    #data = response.content
#
    #with open("data.json", "wb") as f:
    #    f.write(data)

    file = open("data1.json", "r")
    json_data = json.load(file)

    print(type(json_data))

    for key, value in json_data.items():
        print(f"\n key: {key}")
        print(f"Data: {value} \n")




city = input("enter the city name you want to search up on?:  ")

Url(city)
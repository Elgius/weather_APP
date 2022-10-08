from archive import key
import json
import requests


API_KEY = key

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def Url(city):

    URL = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(URL)
    weather_info = response.json

    f = open(response.json, "r")
    data = json.loads(f)

    print(weather_info)


    #if weather_info['cod'] == 200:
    #    kelvin = 273

    #temp = int (weather_info["main"]["temp"])
    #Feels_like_temp= int (weather_info["main"]["Feels_like"])
    #pressure=(weather_info["main"]["Pressure"] )
    #Humidity=(weather_info["main"]["Humidity"] )
    #Wind_speed = (weather_info["main"]["Wind_speed"] * 3.6 )
    #sunrise = (weather_info["sys"]["Sunrise"])
    #sunset = (weather_info["sys"]["Sunset"])
#
    #
    #weather = f"\nWeather of: {city}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {Feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {Humidity}%"
#
    #print(weather)


city = input("enter the city name you want to search up on?:  ")

Url(city)
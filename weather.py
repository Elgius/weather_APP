from archive import key


api_key = key

import argparse

#from configparser import ConfigParser

from urllib import parse
import json


Base_URL = "api.openweathermap.org/data/2.5/weather"



def read_cli_args():

    city = input("Please enter your City name:  ")

    return city

def Build_weather_query (city, imperial = False):
    api_key_name = api_key
    city_name = city

    url = (f"{Base_URL}?q={city_name}"
            f"&appid={api_key_name}")

    return url


if __name__ == "__main__":
    query_url = Build_weather_query()
    print(query_url)
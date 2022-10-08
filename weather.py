from archive import key


api_key = key

import argparse

from configparser import ConfigParser

from urllib import parse



Base_URL = "api.openweathermap.org/data/2.5/weather"



def read_cli_args():

    parser = argparse.ArgumentParser(
        description= "The city data and temperature data"
    )

    parser.add_argument(
        "City", nargs= "+" , type = str , help= "Enter City name"
    )

    parser.add_argument(
        "-i",
        "--imperial",
        action= "store_true",
        help= "Values must be in imperial", 
    )

    return parser.parse_args()

def Build_weather_query ( city_input, imperial = False):
    


if __name__ == "__main__":
    user_args = read_cli_args()
    print(user_args.city , user_args.imperial) 
import string
from archive import key
import json
import requests
from tkinter import *


root =Tk()
root.geometry("400x400")
root.resizable(0,0) 

root.title("Weather App")


API_KEY = key

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city_value = StringVar()

def Url():

    
    city = city_value.get()

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

    #print("What data are you interested in viewing?")
    #print("1. Temperature")
    #print("2. feel like temperature")
    #print("3. Pressure")
    #print("TBA")
    #print("TBA")
    #print("TBA")
    #print("TBA")
    #print("TBA")

    results = str(json_data["main"]["temp"])

    print(results)

    tfield.insert = (INSERT, results)

    file.close()




city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = Url, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)

tfield.pack()

root.mainloop()



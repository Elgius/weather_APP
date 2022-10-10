import json

file = open("data.json", "r")
json_data = json.load(file)

print("What data are you interested in viewing?")
print("1. Temperature")
print("2. feel like temperature")
print("3. Pressure")
print("TBA")
print("TBA")
print("TBA")
print("TBA")
print("TBA")

choice = input("enter required data:  ")

match choice:
    case "1" : print(json_data["main"]["temp"])
    case "2":  print(json_data["main"]["feels_like"])
    case "3" : print(json_data["main"]["pressure"])
    case _:print("Enter the correct value or the data requested not available")

file.close()
import pprint
import json
import requests
api_key = "2b18f6685c5fc803b74f94f086a564d2"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Alexandria"  #input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url).json()

#pprint.pprint(response)

with open('wearher_json.json', 'w') as f:
    json.dump(response, f)

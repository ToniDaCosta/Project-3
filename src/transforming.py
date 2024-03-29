import pandas as pd
import requests
import json
import pandas as pd
from getpass import getpass
from pymongo import MongoClient
import folium

from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster

#  4 SQUAREAPi to retrieve Jsons

def places (venue, lat, lon):
    url = f"https://api.foursquare.com/v3/places/search?query={venue}&ll={lat}%2C{lon}&limit=50"
    headers = {
        "accept": "application/json",
        "Authorization": token
    }
    
    response = requests.get(url, headers=headers).json()
    return response

result = places ("Stadiums", "40.4010201", "-3.7067751")

json_file_path = r"C:\Users\ateso\Desktop\Ironhack\Project-3\Data\Stadiums.json"

with open(json_file_path, "w") as json_file:
    json.dump(result, json_file, indent=2)

print(f"Result has been saved to {json_file_path}")

# Upload Jsons to Mongo DB and Transform them using to_csv function

def to_csv(database_name, collection_name):
   
    client = MongoClient("localhost:27017")
    db = client[database_name]
    c = db[collection_name]

    filter_ = {
        "results.name": {"$exists": True},
        "results.geocodes.main": {"$ne": None}
    }

    projection = {
        "results.name": 1,
        "results.geocodes.main": 1
    }

    sorting = [("results.0.name", 1)]

    result_cursor = c.find(filter_, projection).sort(sorting)
    result_list = list(result_cursor)

   
    names_and_coordinates = [
        (item['name'], item['geocodes']['main']['latitude'], item['geocodes']['main']['longitude'])
        for item in result_list[0]['results']
    ]

  
    df = pd.DataFrame(names_and_coordinates, columns=['Name', 'Latitude', 'Longitude'])

  
    df.to_csv("C:\\Users\\ateso\\Desktop\\Ironhack\\Project-3\\Data\\acsv\\new_csv.csv", index=False)

    # Used to find information from "Companies" data set.

    
client = MongoClient("localhost:27017")
db = client[database_name]
c = db[collection_name]

def company_city(database_name, collection_name):

    filter_2 = {"name": {"$exists": True}, "offices.city": "Barcelona", "category_code": "games_video"}
    projection = {"name": 1, "offices.city": 1, "category_code": 1, "offices.latitude": 1, "offices.longitude": 1}
    sorting = [("name", 1)]

    result_list = list(c.find(filter_2, projection).sort(sorting))

    names_and_coordinates = []
    for item in result_list:
        if 'offices' in item and item['offices']:
            for office in item['offices']:
                latitude = office.get('latitude')
                longitude = office.get('longitude')
                if latitude is not None and longitude is not None:
                    names_and_coordinates.append((item['name'], latitude, longitude))

    df = pd.DataFrame(names_and_coordinates, columns=['Name', 'Latitude', 'Longitude'])

    csv_filename = "C:\\Users\\ateso\\Desktop\\Ironhack\\Project-3\\Data\\acsv\\new_csv.csv"
    df.to_csv(csv_filename, index=False)

    print(f"Data exported to {csv_filename}")
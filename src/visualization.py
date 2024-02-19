import requests
import json
import pandas as pd
from getpass import getpass
from pymongo import MongoClient
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
import os
"""
I have created several views of different maps.

Here all the functions and general maps used, please note that are file origin path dependant.

"""

def create_gym_map(csv_file_path):
  
    df_gym = pd.read_csv(csv_file_path)

 
    map_center = [df_gym['Latitude'].mean(), df_gym['Longitude'].mean()]

    
    gym_map = folium.Map(location=map_center, zoom_start=13)


    for index, row in df_gym.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='red', icon='dumbbell', prefix='fa')
        ).add_to(gym_map)

    return gym_map

def create_bars_map (csv_file_path):
    
    df_bars = pd.read_csv(csv_file_path)

    map_center = [df_bars['Latitude'].mean(), df_bars['Longitude'].mean()]

    bars_map = folium.Map(location=map_center, zoom_start=13)

    for index, row in df_bars.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='blue', icon='beer', prefix='fa')
        ).add_to(bars_map)


    return bars_map

def create_restaurants_map (csv_file_path):
    
    df_restaurants = pd.read_csv(csv_file_path)

    map_center = [df_restaurants['Latitude'].mean(), df_restaurants['Longitude'].mean()]

    restaurants_map = folium.Map(location=map_center, zoom_start=13)

    for index, row in df_restaurants.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='lightblue', icon='utensils', prefix='fa')
        ).add_to(restaurants_map)


    return restaurants_map

def create_schools_map (csv_file_path):
    
    df_schools = pd.read_csv(csv_file_path)

    map_center = [df_schools['Latitude'].mean(), df_schools['Longitude'].mean()]

    schools_map = folium.Map(location=map_center, zoom_start=16)

    for index, row in df_schools.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='lightred', icon='school', prefix='fa')
        ).add_to(schools_map)


    return schools_map

def create_others_map (csv_file_path):
    
    df_others = pd.read_csv(csv_file_path)

    map_center = [df_others['Latitude'].mean(), df_others['Longitude'].mean()]

    others_map = folium.Map(location=map_center, zoom_start=16)

    for index, row in df_others.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='orange', icon='building-columns', prefix='fa')
        ).add_to(others_map)


    return others_map

# This city_map includes all the 5 layers with previous maps.

def generate_city_map(city, lat, lon, data_path):

    df = pd.read_csv(data_path)
    df['Local_type'] = df['Local_type'].str.capitalize()

    city_map = folium.Map(location=[lat, lon], zoom_start=15)

    bar_group = folium.FeatureGroup(name='Bars')
    gym_group = folium.FeatureGroup(name='Gyms')
    school_group = folium.FeatureGroup(name='Schools')
    restaurant_group = folium.FeatureGroup(name='Restaurants')
    others_group = folium.FeatureGroup(name='Others')

    for index, row in df.iterrows():
        Local_type = row["Local_type"]
        Name = row["Name"]
        latitude = row["Latitude"]
        longitude = row["Longitude"]

        if Local_type == "Bar":
            icon = folium.Icon(color='blue', icon_color='black', icon='beer', prefix='fa')
            marker = folium.Marker(
                location=[latitude, longitude],
                icon=icon,
                tooltip=f"{Local_type}: {Name}"
            )
            marker.add_to(bar_group)

        elif Local_type == "Gym":
            icon = folium.Icon(color='red', icon_color='white', icon='dumbbell', prefix='fa')
            marker = folium.Marker(
                location=[latitude, longitude],
                icon=icon,
                tooltip=f"{Local_type}: {Name}"
            )
            marker.add_to(gym_group)

        elif Local_type == "Schools":
            icon = folium.Icon(color='lightred', icon_color='white', icon='school', prefix='fa')
            marker = folium.Marker(
                location=[latitude, longitude],
                icon=icon,
                tooltip=f"{Local_type}: {Name}"
            )
            marker.add_to(school_group)

        elif Local_type == "Restaurants":
            icon = folium.Icon(color='lightblue', icon_color='white', icon='utensils', prefix='fa')
            marker = folium.Marker(
                location=[latitude, longitude],
                icon=icon,
                tooltip=f"{Local_type}: {Name}"
            )
            marker.add_to(restaurant_group)

        elif Local_type == "Others":
            icon = folium.Icon(color='orange', icon_color='white', icon='building-columns', prefix='fa')
            marker = folium.Marker(
                location=[latitude, longitude],
                icon=icon,
                tooltip=f"{Local_type}: {Name}"
            )
            marker.add_to(others_group)

        else:
            print(f"Unknown Local_type: {Local_type}")
            continue

    bar_group.add_to(city_map)
    gym_group.add_to(city_map)
    school_group.add_to(city_map)
    restaurant_group.add_to(city_map)
    others_group.add_to(city_map)

   
    folium.LayerControl().add_to(city_map)

    return city_map

city_map = generate_city_map("Athens", 37.9871384, 23.7183808, r"C:\Users\ateso\Desktop\Ironhack\Project-3\Data\Athens\Athens_all_data_300\Athens_data.csv")
city_map

# This map creates a single HeatMap.

def create_heatmap(csv_file_path):
    df_bars = pd.read_csv(csv_file_path)

    map_center = [df_bars['Latitude'].mean(), df_bars['Longitude'].mean()]

    bars_map = folium.Map(location=map_center, zoom_start=13)

   
    locations = df_bars[['Latitude', 'Longitude']].values.tolist()

  
    HeatMap(locations).add_to(bars_map)

    return bars_map

"""
This code takes 2 CSV file paths as result of the exported data to CSV files.

Note: csv_all_path is meant to contain all the combined data from venues obtained from 4squareAPi.

Note: csv_off_path is meant to contain the information found in "companies" data set.

"""

def heat_combined(csv_all_path, csv_off_path):

    df_Paris_all = pd.read_csv(csv_all_path)
    df_Paris_off = pd.read_csv(csv_off_path)
    
    map_center = [df_Paris_all['Latitude'].mean(), df_Paris_all['Longitude'].mean()]
    heat_combined = folium.Map(location=map_center, zoom_start=13)

    marker_group = folium.FeatureGroup(name='Company to purchase').add_to(heat_combined)

    for index, row in df_Paris_off.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='green', icon='dollar', prefix='fa')
        ).add_to(marker_group)

    
    locations_all = df_Paris_all[['Latitude', 'Longitude']].values.tolist()
    HeatMap(locations_all, name="Area Density").add_to(heat_combined)

    
    radius = 4000
    folium.Circle(
        location=map_center,
        radius=radius,
        color='blue',
        fill=True,
        fill_color='none',
        fill_opacity=0.3
    ).add_to(heat_combined)

  
    folium.LayerControl(name="Area Density").add_to(heat_combined)

    return heat_combined
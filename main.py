from pandas import json_normalize
import src.extracting as ext
import src.visualization as viz
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
import pandas as pd
from getpass import getpass
from pymongo import MongoClient
import folium
import os
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import src.extracting as ext
import src.visualization as viz


# Select venue, latitude and longitude. Result will be sent to the "json_file path, update as needed"

ext.places () # venue, lat, lon

ext.to_csv() # database_name, collection_name from MONGODB Data Sets

ext.company_city() #database_name, collection_name from MONGODB using Companies Data Set.

viz.create_gym_map() # csv_file_path

viz.create_bars_map() # csv_file_path

viz.create_restaurants_map() # csv_file_path

viz.create_schools_map() # csv_file_path

viz.create_others_map() # csv_file_path

viz.generate_city_map() # csv_file_path

viz.create_heatmap() # csv_file_path

viz.heat_combined() # csv_all_cities_path, csv_office_path "From companies"
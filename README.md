# Project-3 Move ON "GeoSpatial Data Project"

Welcome to Project-3. In this project, we are presented with the task of finding a suitable city and spot to relocate our support team.

The company will have the following scheme:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Analysts
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy who loves basketball
- 10 Executives
- 1 CEO/President.

# As data analysts, we were tasked with the job of finding a place that meets some of the people's preferences.

- Designers like to attend design talks and share knowledge. There must be some nearby companies that also focus on design.
- 30% of the company staff have at least 1 child.
- Developers prefer to be near successful tech startups that have raised at least 1 Million dollars.
- Executives love Starbucks A LOT. Ensure there's a Starbucks not too far.
- Account managers need to travel a lot.
- Everyone in the company is between 25 and 40, so give them a place to go party.
- The CEO is vegan.
- To make the maintenance guy happy, a basketball stadium must be around 10 km.
- The office dog, "Dobby," needs a hairdresser every month. Ensure there's one not too far away.

# For this project, we used the following tools:

- MongoDB: [https://docs.mongodb.com/manual/geospatial-queries/]
- Foursquare API: [https://developer.foursquare.com/]

# We also used the following Libraries:

- import matplotlib.pyplot as plt
- import seaborn as sns
- import requests
- import json
- import pandas as pd
- from getpass import getpass
- from pymongo import MongoClient
- import folium
- import os
- from folium import Choropleth, Circle, Marker, Icon, Map
- from folium.plugins import HeatMap, MarkerCluster

# After considering some cities to sample in the EU, we came up with 5 main cities: Madrid, Barcelona, Paris, Lisbon, and Athens.

We approached the cities one by one, extracting samples from Foursquare to determine the radius and concentrations of business activities in the cities.

- Restaurants
- Schools
- Gyms
- Parks
- Coffee shops & Bars
- Stadiums

# We created a map view with all these layers to interact as a first step.

![alt text](<Bars Barcelona-1.png>)

This process was replicated for the other 4 cities in this project. Additionally, another type of map was used as a "HeatMap" to better appreciate the concentration of the volume, and a layer with a 4km square radius was added to verify the proximity of the results.

# The HeatMap determined the concentration level of the cities and their quarters with the most activity.

![alt text](BCN-1.png)

These maps revealed the concentration area of each city, and that the most suitable places are closer to the radius center, but it was not enough to decide yet what was the most optimal city to move to.

# Taking other companies as a reference in the cities, considering perhaps buying one of them.

![alt text](<Barcelona Radious-1.png>)

After exploring a record of data based on companies with tags "Gaming or Software," we decided to add another layer with all the companies found in each city, by adding a green marker.

This last step also gave a certain validation point to our previously conceived idea: most of the companies in these cities are in the 4km radius from the center.

# Paris came up as the city with the most companies found out of the 5 cities, and most of the companies are in the same radius.

![alt text](<Paris Radious-2.png>)

# Independent Location Decision within a 4km Radius Square:

This suggests that our decision is to be taken within a 4km radius for our business. We also need to consider the following factors:

- Accessibility: Ensure the location is easily accessible for customers, employees, and suppliers.
- Demographics: Analyze the local population and potential customer base.
- Competition: Evaluate the level of competition in the area.
- Cost: Assess the cost of acquiring or leasing property in the selected square.

# Consideration of Purchasing a Company in a Specific City:

This option involves acquiring an already established business in a particular city. Key considerations include:

- Industry: Ensure that the purchased company aligns with your business goals and industry.
- Financials: Analyze the financial health and performance of the company.
- Reputation: Consider the reputation of the existing business in the local market.
- Legal and Regulatory Compliance: Verify that the company complies with all legal and regulatory requirements.

Before making a decision, it's crucial to conduct thorough research and possibly seek professional advice. Additionally, creating a detailed business plan that outlines your goals, target market, and financial projections can help guide your decision-making process.

Remember to weigh the pros and cons of each option, considering factors such as initial investment, ongoing operational costs, potential for growth, and long-term sustainability.

# Coding structure and files:

For this project we decided to separate all the images and some specific steps taken in several files for each city:

- Data: with a file per city containing all the Jsons downloaded from 4Square.APi, and later used to substract the information by using MONGO DB.

- acsv : is the file created to organize the data taken using Mongo Queries with python.

- Images : File containing all the screenshots taken for presentations and others.

- src : File containing all the coding data for "transformation" and "visualizations".

- Visualizations: File with all the raw code in Jupiter files.
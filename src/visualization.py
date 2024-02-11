def folium_map_gym (csv_file_path):
    
    df = pd.read_csv(csv_file_path)
   
    map_center = [df['Latitude'].mean(), df['Longitude'].mean()]

    my_map = folium.Map(location=map_center, zoom_start=13)

    for index, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='red', icon='dumbbell', prefix='fa')
        ).add_to(my_map)

    return my_map
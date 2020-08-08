import folium
import pandas
data=pandas.read_csv("cities.csv")
lat=list(data["Latitude"])
lon=list(data["Longitude"])
col=list(data["color"])
city=list(data["Place"])
map=folium.Map(location=(12.58,77.48),zoom_start=4)
fg=folium.FeatureGroup(name="metro_map")
for lt,ll,city_name,clr in zip(lat,lon,city,col):
    fg.add_child(folium.Marker(location=(lt,ll),popup=city_name, icon=folium.Icon(color=clr)))
map.add_child(fg)
map.save('map_metro.html')
#!/usr/bin/env python3
import requests
import folium
from geopy.geocoders import Nominatim
map=folium.Map(location=[41.903853, 12.484492],zoom_start=6)
folium.TileLayer('stamenterrain').add_to(map)
cities=["bari","l'aquila","potenza","catanzaro","napoli","bologna","trieste","roma","genova","milano","ancona","campobasso","torino","cagliari","palermo","firenze","trento","perugia","aosta","venezia"]
url='http://api.openweathermap.org/data/2.5/weather?appid=39411ec0a72cb5c7b070e9da15555979&q='
#city=url+"perugia, IT"
for a in cities:
	a=a+", IT"
	city=url+a
	jdata=requests.get(city).json()
	fd=jdata['weather'][0]['description']
	fd2=jdata['main']['temp']
	fd2=fd2-273.15
	fd2=int(fd2)
	fd2=str(fd2)
	print(a+": "+fd+" "+fd2+"°")
	geolocator = Nominatim()
	location = geolocator.geocode(a)
	folium.Marker([location.latitude, location.longitude],popup=fd2).add_to(map)
	print(location.latitude, location.longitude)
	print("-------------------------------------------------")
map.save('meteo.html')

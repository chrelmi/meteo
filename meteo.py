#!/usr/bin/env python3
import requests
url='http://api.openweathermap.org/data/2.5/weather?appid=39411ec0a72cb5c7b070e9da15555979&q='
city=url+"perugia, IT"
jdata=requests.get(city).json()
fd=jdata['weather'][0]['description']
fd2=jdata['main']['temp']
fd2=fd2-273.15
fd2=int(fd2)
fd2=str(fd2)
print(jdata)
print("-------------------------------------------------")
print(fd+" "+fd2)

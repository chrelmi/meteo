#!/usr/bin/env python3
import requests
import time
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
time.sleep(5)
print(fd+" "+fd2)





"""
sfruttare time.sleep(ogni 3 ore) e mandare il programma in loop per evitare di usare il corntab-
integrare la grfica qui
cambiare l'aspetto delle scritte
"""

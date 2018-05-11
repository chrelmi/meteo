#!/usr/bin/env python3
import requests
import time
url='http://brunisciarp.ddns.net/domotica/getData.php'
jdata=requests.get(url).json()
fd=jdata[0]
jdata2=fd['nome']
jdata3=fd['stato']
jdata3= int(jdata3)
#fd2=jdata['stato']
#print(jdata)
if jdata3==0:
	time.sleep(5)
	jdata3=1
print("-------------------------------------------------")
jdata2=str(jdata2)
r = requests.put('http://brunisciarp.ddns.net/domotica/setData.php/?nome=TV1&stato=1')
jdata3=str(jdata3)
print(jdata2 + jdata3)

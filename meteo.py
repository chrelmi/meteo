#!/usr/bin/env python3
import requests
import time
import tkinter
from tkinter import *
import csv
url='http://api.openweathermap.org/data/2.5/weather?appid=39411ec0a72cb5c7b070e9da15555979&q='
city=url+"Perugia, IT"
def update():
	jdata=requests.get(city).json() #richiesta del json
	fd=jdata['weather'][0]['description'] #memorizzazione delle informazioni
	fd2=jdata['main']['temp']
	fd2=fd2-273.15 #temperatura convertita da K a °C
	fd2=int(fd2)
	fd2=str(fd2)
	print("-------------------------------------------------")
	print(fd+" "+fd2)
	prev=fd+" "+fd2+"° C"
	l3.config(text=prev)
	with open('list.csv') as csvfile: #file csv contenente tutte le possibili opzioni meteo che sito fornisce
		r=csv.DictReader(csvfile)
		for row in r:
			name=row['nome']
			im=row['img'] #estrazioe dell'icona in funzione della descrizione meteo
			if name==fd:
				img.config(file=im)
	l.after(3600000,update) #aggiornamento della funzione
	#10800000(3 ore)
	#3600000(1 ora)
def tick(time1=''): #funzione clock
	time2=time.strftime("%A %d %B\n %H:%M:%S") #giorno della settimana, numero del giorno, mese, orario
	time2=str(time2)
	if time2!= time1:
		time1=time2
		t.config(text=time2)
	t.after(200,tick)
window=Tk() #interfaccia grafica
window.title("Stazione Meteo")
window.geometry("800x400")
window.configure(background="#000000")
l=tkinter.Label(window,text="Perugia, IT",bg="#000000",fg="#FFFFFF")
l3=tkinter.Label(window, text="", bg="#000000", fg="#FFFFFF")
l3.config(font=("OpenDyslexic",22))
l.config(font=("Noto Sans Mono CJK JP Bold", 44))
l.grid(row=0,column=0, padx=50)
l3.grid(row=1,column=0, padx=20)
img=tkinter.PhotoImage(file="rain.png")
l2=tkinter.Label(window,image=img,bg="#000000")
l2.grid(row=0, column=1, padx=100)
t=tkinter.Label(window, bg="#000000", fg="#FFFFFF")
t.config(font=("Courier 10 Pitch",32))
t.grid(row=2,column=0)
update()
tick()
window.mainloop()

#!/usr/bin/env python3
import requests
import time
import tkinter
from tkinter import *
url='http://api.openweathermap.org/data/2.5/weather?appid=39411ec0a72cb5c7b070e9da15555979&q='
city=url+"Perugia, IT"
def update():
	jdata=requests.get(city).json()
	fd=jdata['weather'][0]['description']
	fd2=jdata['main']['temp']
	fd2=fd2-273.15
	fd2=int(fd2)
	fd2=str(fd2)
	print("-------------------------------------------------")
	print(fd+" "+fd2)
	prev=fd+" "+fd2+"° C"
	l3.config(text=prev)
	l.after(60000,update)
	img.config(file="clouds.png")
	#10800000(3 ore)
def tick(time1=''):
	time2=time.strftime("%H:%M:%S")
	time2=str(time2)
	if time2!= time1:
		time1=time2
		t.config(text=time2)
	t.after(1000,tick)

window=Tk()
window.title("Stazione Meteo")
window.geometry("800x400")
window.configure(background="#000000")
l=tkinter.Label(window,text="Perugia, IT",bg="#000000",fg="#FFFFFF")
l3=tkinter.Label(window, text="", bg="#000000", fg="#FFFFFF")
l3.config(font=("OpenDyslexic",22))
l.config(font=("Noto Sans Mono CJK JP Bold", 44))
l.grid(row=0,column=0, padx=50)
l3.grid(row=1,column=0, padx=20)
img=tkinter.PhotoImage(file="sereno.png")
l2=tkinter.Label(window,image=img,bg="#000000")
l2.grid(row=0, column=1, padx=100)
t=tkinter.Label(window, bg="#000000", fg="#FFFFFF")
t.config(font=("Noto Sans Mono CJK JP Bold",32))
t.grid(row=2,column=0)
update()
tick()
window.mainloop()

"""
sfruttare time.sleep(ogni 3 ore) e mandare il programma in loop per evitare di usare il corntab-
integrare la grfica qui
cambiare l'aspetto delle scritte
"""

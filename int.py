#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
import time
def tick(time1=''):
	time2=time.strftime("%H:%M:%S")
	time2=str(time2)
	if time2!= time1:
		time1=time2
		l.config(text=time2)
	l.after(1000,tick)
	print("bon")
root=tk.Tk()
root.title("interfaccia con aggiornamento")
l=tk.Label(root,bg='black',fg='green')
l.pack()
root.geometry('500x400')
tick()
root.mainloop()


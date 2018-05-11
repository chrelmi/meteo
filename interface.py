#!/usr/bin/env python3
import tkinter
from tkinter import *
window=Tk()
window.title("Stazione Meteo")
window.geometry("800x400")
window.configure(background="#000000")
l=tkinter.Label(window,text="Perugia",bg="#000000",fg="#FFFFFF")
l3=tkinter.Label(window, text="Scattered clouds   20°C", bg="#000000", fg="#FFFFFF")
l3.config(font=("tlwgmono",22))
l.config(font=("verdana", 44))
l.grid(row=0,column=0, padx=50)
l3.grid(row=1,column=0, padx=20)
img=tkinter.PhotoImage(file="rain.png")
l2=tkinter.Label(window,image=img,bg="#000000")
l2.grid(row=0, column=1, padx=100, rowspan=2, pady=40)
window.mainloop()

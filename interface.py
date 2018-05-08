#!/usr/bin/env python3
import tkinter
from tkinter import *
window=Tk()
window.title("Stazione Meteo")
window.geometry("700x600")
window.configure(background="#000000")
l=tkinter.Label(window,text="Perugia",bg="#000000",fg="#FFFFFF")
l.pack()
img=tkinter.PhotoImage(file="sereno.png")
l2=tkinter.Label(window,image=img,bg="#000000")
l2.pack()


window.mainloop()

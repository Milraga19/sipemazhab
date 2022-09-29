from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import login
from add_data import *
from login import *
import sys

def alert_login():
    top = Toplevel()
    top.geometry("300x50")
    top.title("Alert!")
    Label(top, text="Username atau Password salah!", font=("Montserrat 10")).place(x=40,y=15)


def auth(username, password):
    sukses = False
    file = open("users.txt", "r")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a==username and b==password):
            sukses = True
            break
    file.close
    if(sukses):
        # print("masukmi")
        Add_data()
    else:
        # print("aih ndamasuk")
        alert_login()
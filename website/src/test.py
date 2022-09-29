from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from login import *
from search import *
# from test import *
import sys
sys.setrecursionlimit(9000)

root = Tk()
root.title("Sistem Pencarian Hukum Fiqih")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("1366x768")   #("%dx%d" % (width, height))
root.state('zoomed')

## Function untuk resize image

def resize_image(event):
    new_width = 1366
    new_height = 768
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo

## gambar yang dapat di resize

image = Image.open(r'bgg/homebgnew2.png') #background awal
global copy_of_image
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

## function

def login():
    Auth()
    # Add_data()

def search():
    Search_data()

## tombol
#fg="",,'bold italic'
#user_label = Label(root, bg="#6A8BFF", fg="#F2F2F2", text="Menu")
#user_label.config(font=("Poppins", 16))
#user_label.place(relx=0.235, rely=0.3, anchor=CENTER)
search_data_button = Button(root,bg="#4090A9", fg="#F2F2F2", bd=0,activebackground="#75B9CE",
                      font=("Montserrat", 13, 'bold'),
                      text='Cari Hukum', padx=8, pady=8, command = search)
search_data_button.place(x=166, y=549, anchor=CENTER, height=50, width=190)

login_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                     font=("Montserrat", 13, 'bold'), text='Login Admin',
                     padx=8, pady=8, command = login)
login_button.place(x=1233, y=30, anchor=CENTER, height=50, width=190)

quit = Button(root, bg="#F2F2F2", fg="#4090A9", bd=0,activebackground="#75B9CE",
              font=("Montserrat", 13, 'bold'),
              text="Keluar", command=root.destroy, padx=8, pady=8)
quit.place(x=366, y=549, anchor=CENTER, height=50, width=190)

root.mainloop()

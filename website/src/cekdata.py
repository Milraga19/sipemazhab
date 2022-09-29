import pathlib
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from add_data import *

from PIL import Image, ImageTk
import shutil
from docx2pdf import convert
from io import StringIO

import sys
import glob
import subprocess, os


def info(message, title="Pemberitahuan"):
    root = Tk()
    root.iconify()
    showinfo(title, message, parent=root)
    root.destroy()


sys.setrecursionlimit(9000)

fname = ''


def add_data():
    Add_data()

class Cek_data:
    def __init__(self):
        root = Toplevel()
        root.title("Cek Data")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("1366x768")  # ("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image

        image = Image.open(r'bgg/tambahbgnew.png')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        tambah_button = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, activebackground="#6A8BFF",
                               font=("Montserrat", 16, 'bold'),
                               text="Tambah Data", command=root.destroy, padx=8, pady=8)
        tambah_button.place(relx=0.09, rely=0.3, anchor=CENTER, height=50, width=200)

        cek_button = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, activebackground="#6A8BFF",
                            font=("Montserrat", 16, 'bold'),
                            text="Cek Data", command=Cek_data, padx=8, pady=8)
        cek_button.place(relx=0.09, rely=0.4, anchor=CENTER, height=50, width=200)

        quit = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, activebackground="#6A8BFF",
                      font=("Montserrat", 16, 'bold'),
                      text="Kembali", command=root.destroy, padx=8, pady=8)
        quit.place(relx=0.09, rely=0.5, anchor=CENTER, height=50, width=200)

        cekpdf_button = Button(root, text="Data PDF", bg="#6A8BFF", fg="#F2F2F2", bd=0, font=("Montserrat", 15, 'bold'),
                              command=self.cekpdf)
        cekpdf_button.place(relx=0.662, rely=0.287, anchor=W, width=150, height=50)

        cektxt_button = Button(root, text="Data Txt", bg="#6A8BFF", fg="#F2F2F2", bd=0,
                              font=("Montserrat", 15, 'bold'), command=self.cektxt)
        cektxt_button.place(relx=0.662, rely=0.4, anchor=W, width=150, height=50)

        root.mainloop()

    ## Class for a placeholder

    class EntryWithPlaceholder(Entry):
        def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', textvariable=None):
            super().__init__(master, textvariable=textvariable)

            self.placeholder = placeholder
            self.placeholder_color = color
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.foc_in)
            self.bind("<FocusOut>", self.foc_out)

            self.put_placeholder()

        def put_placeholder(self):
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

        def foc_in(self, *args):
            if self['fg'] == self.placeholder_color:
                self.delete('0', 'end')
                self['fg'] = self.default_fg_color

        def foc_out(self, *args):
            if not self.get():
                self.put_placeholder()

    ## Function for resizing the Image

    def resize_image(self, event):
        new_width = 1366
        new_height = 768
        global copy_of_image
        image = copy_of_image.resize((new_width, new_height))
        global photo
        photo = ImageTk.PhotoImage(image)
        global label
        label.config(image=photo)
        label.image = photo

    ## Process\

    def cekpdf(self):
        subprocess.Popen(r'explorer /select,"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\data_pdf\1.pdf"')

    def cektxt(self):
        subprocess.Popen(r'explorer /select,"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\data_txt\1.txt"')

    # def train(self):
    #     parse()
    #     info('Sukses Membuat Inverted Index')


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from search_func import *
from testlogin import *
from search import *
import os
import subprocess


# def display_text(doc):
#     filename = 'data_txt/%d.txt' % (doc)
#
#     with open(filename, 'r') as f:
#         f.read(100)


class kelas_hasil:
    def __init__(self, name,bobot,queries, ext_time):
        root = Toplevel()
        root.title("Hasil Pencarian")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("1366x768")  # ("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image

        image = Image.open(r'bgg/hasilquerynew.png')
        # image = Image.open(r'bgg/contoh.jpg')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        def display_text(doc,queries):
            filename = 'data_txt/%d.txt' % (doc)
            f = open(filename, "r", encoding="UTF8").readlines(100)
            # print(f)
            # f[2] = f[2].replace("\n", "...")
            # new_f = (''.join(f))
            new_f = f[0],f[1],"\n"
            # print(f)
            new_f2 = (''.join(new_f))
            cari = list(queries.split())
            with open('data_txt/%d.txt'%(doc), 'r+') as f:
                for line in f:
                    for i in range(len(cari)):
                        if cari[i] in line:
                            a = line.split("\n")
                            a[1] = a[1].replace('', '...')
                            break
                        else:
                            continue
                        i+=1
            new_a =(''.join(a))
            new_arr=new_f2,new_a
            new_arr2=(''.join(new_arr))
            return new_arr2

        quit = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                      font=("Montserrat", 13, 'bold'),
                      text="Kembali", command=root.destroy, padx=8, pady=8)
        quit.place(x=1233, y=30, anchor=CENTER, height=50, width=190)

        hasil_query = Label(root, text="Hasil Pencarian Query : "+queries, font=("Montserrat", 13, 'bold'), bg='grey', fg='white', padx=3, pady=3)
        hasil_query.place(relx=0.508, rely=0.01, anchor=N)
        ext_query = Label(root, text="Waktu Eksekusi : " + str(ext_time) + " Detik", font=("Montserrat", 6, 'bold'), bg='grey',
                            fg='white', padx=3, pady=3)
        ext_query.place(relx=0.508, rely=0.05, anchor=N)

        user_name = Label(root, text=display_text(name[0],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black', justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.050, rely=0.108)#240
        user_id = Label(root, text="DOC ID : "+str(name[0]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.050, rely=0.230)#240
        user_bobot = Label(root, text="Similarity : "+str(bobot[0]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_bobot.place(relx=0.090, rely=0.230)#165
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda : self.openfile(name[0],queries)), padx=8, pady=8)
        cari_button.place(x=129, y=208, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda :self.openbook(name[0])), padx=8, pady=8)
        buku_button.place(x=259, y=208, anchor=CENTER, height=50, width=120)

        user_name = Label(root, text=display_text(name[1],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.050, rely=0.348)  # 0.10 - 0.02
        user_id = Label(root, text="DOC ID : " + str(name[1]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.050, rely=0.470)  # 0.209 - 0.021
        user_bobot = Label(root, text="Similarity : " + str(bobot[1]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.090, rely=0.470)  # 175 - 14
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[1])), padx=8, pady=8)
        cari_button.place(x=129, y=373, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[1])), padx=8, pady=8)
        buku_button.place(x=259, y=373, anchor=CENTER, height=50, width=120)

        user_name = Label(root, text=display_text(name[2],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.050, rely=0.588)  # 0.10 - 0.02
        user_id = Label(root, text="DOC ID : " + str(name[2]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.050, rely=0.710)  # 0.209 - 0.021
        user_bobot = Label(root, text="Similarity : " + str(bobot[2]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.090, rely=0.710)  # 175 - 14
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[2])), padx=8, pady=8)
        cari_button.place(x=129, y=543, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[2])), padx=8, pady=8)
        buku_button.place(x=259, y=543, anchor=CENTER, height=50, width=120)




        user_name = Label(root, text=display_text(name[3],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.350, rely=0.108)  # 240
        user_id = Label(root, text="DOC ID : " + str(name[3]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.350, rely=0.230)  # 240
        user_bobot = Label(root, text="Similarity : " + str(bobot[3]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.390, rely=0.230)  # 165
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[3])), padx=8, pady=8)
        cari_button.place(x=539, y=208, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[3])), padx=8, pady=8)
        buku_button.place(x=669, y=208, anchor=CENTER, height=50, width=120)

        user_name = Label(root, text=display_text(name[4],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.350, rely=0.348)  # 0.10 - 0.02
        user_id = Label(root, text="DOC ID : " + str(name[4]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.350, rely=0.470)  # 0.209 - 0.021
        user_bobot = Label(root, text="Similarity : " + str(bobot[4]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.390, rely=0.470)  # 175 - 14
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[4])), padx=8, pady=8)
        cari_button.place(x=539, y=373, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[4])), padx=8, pady=8)
        buku_button.place(x=669, y=373, anchor=CENTER, height=50, width=120)

        user_name = Label(root, text=display_text(name[5],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.350, rely=0.588)  # 0.10 - 0.02
        user_id = Label(root, text="DOC ID : " + str(name[5]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.350, rely=0.710)  # 0.209 - 0.021
        user_bobot = Label(root, text="Similarity : " + str(bobot[5]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.390, rely=0.710)  # 175 - 14
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[5])), padx=8, pady=8)
        cari_button.place(x=539, y=543, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[5])), padx=8, pady=8)
        buku_button.place(x=669, y=543, anchor=CENTER, height=50, width=120)


        user_name = Label(root, text=display_text(name[6],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.650, rely=0.108)  # 240
        user_id = Label(root, text="DOC ID : " + str(name[6]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.650, rely=0.230)  # 240
        user_bobot = Label(root, text="Similarity : " + str(bobot[6]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.690, rely=0.230)  # 165
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[6])), padx=8, pady=8)
        cari_button.place(x=949, y=208, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[6])), padx=8, pady=8)
        buku_button.place(x=1079, y=208, anchor=CENTER, height=50, width=120)

        user_name = Label(root, text=display_text(name[7],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.650, rely=0.348)  # 0.10 - 0.02
        user_id = Label(root, text="DOC ID : " + str(name[7]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.650, rely=0.470)  # 0.209 - 0.021
        user_bobot = Label(root, text="Similarity : " + str(bobot[7]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.690, rely=0.470)  # 175 - 14
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[7])), padx=8, pady=8)
        cari_button.place(x=949, y=373, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[7])), padx=8, pady=8)
        buku_button.place(x=1079, y=373, anchor=CENTER, height=50, width=120)

        user_name = Label(root, text=display_text(name[8],queries), font=("Montserrat", 9, 'bold'), bg='white', fg='black',
                          justify=LEFT, wraplength=330, padx=3, pady=3)
        user_name.place(relx=0.650, rely=0.588)  # 0.10 - 0.02
        user_id = Label(root, text="DOC ID : " + str(name[8]), font=("Montserrat", 7, 'italic'), bg='white', fg='black')
        user_id.place(relx=0.650, rely=0.710)  # 0.209 - 0.021
        user_bobot = Label(root, text="Similarity : " + str(bobot[8]), font=("Montserrat", 7, 'italic'), bg='white',
                           fg='black')
        user_bobot.place(relx=0.690, rely=0.710)  # 175 - 14
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat Dokumen", command=(lambda: self.openfile(name[8])), padx=8, pady=8)
        cari_button.place(x=949, y=543, anchor=CENTER, height=50, width=120)
        buku_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                             font=("Montserrat", 9, 'bold'),
                             text="Lihat di Buku", command=(lambda: self.openbook(name[8])), padx=8, pady=8)
        buku_button.place(x=1079, y=543, anchor=CENTER, height=50, width=120)


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

    def openfile(self, name,queries):
        import fitz

        ## READ IN PDF
        doc = fitz.open("data_pdf/%d.pdf" % (name))

        for page in doc:
            ### SEARCH
            text = list(queries.split(" "))
            text_instances = [page.search_for(text) for text in text]

            ### HIGHLIGHT
            for inst in text_instances:
                highlight = page.add_highlight_annot(inst)
                highlight.update()

        ### OUTPUT
        doc.save("output.pdf", garbage=4, deflate=True, clean=True)
        os.startfile('D:\Yoga Punya\\tugas\SEMESTER 7\STKI\\testfile\output.pdf')

    def openbook(self,name):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        import pyautogui
        import time

        filename = 'data_txt/%d.txt' % (name)
        f = open(filename, "r", encoding="UTF8").readlines(100)
        # print(f)
        # f[0] = f[0].replace("   ", "")
        # new_f = (''.join(f))
        new_f = f[0].strip()

        # set chromodriver.exe path
        chrome_opt = Options()
        chrome_opt.add_experimental_option("detach", True)
        PATH = 'D:\Yoga Punya\\tugas\chromedriver.exe'

        web = webdriver.Chrome(PATH, chrome_options = chrome_opt)
        web.get(
            'file:///D:/Yoga%20Punya/tugas/Bahan%20Final%20Battle/Buku%20Ar-Risalah/Terjemah%20Fiqih%204%20Madzhab%20Jilid%201.pdf')
        web.maximize_window()

        time.sleep(10)

        pyautogui.scroll(-100)

        # time.sleep(10)

        pyautogui.hotkey('ctrl', 'f')
        pyautogui.typewrite(new_f)
        pyautogui.hotkey('Return')


def final_result(name,bobot,queries,ext_time):
    print(name,bobot,queries, ext_time)
    b = kelas_hasil(name,bobot,queries, ext_time)



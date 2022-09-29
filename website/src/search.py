from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from search_func import *
from testlogin import *
from tampilan_hasil import *

import time

sys.setrecursionlimit(9000)

fname = ''



class Search_data:
    def __init__(self):
        root = Toplevel()
        root.title("Cari Data")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("1366x768")  # ("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image

        image = Image.open(r'bgg/caribgnew2.png')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        ## Adding TextBoxes

        # user_label = Label(root, bg="white", fg="#5DB8EC", text="Nama Dokumen")
        # user_label.config(font=("Montserrat", 20))
        # user_label.place(relx=0.416, rely=0.489, anchor='w')
        global v1
        v1 = StringVar()
        user_entry = self.EntryWithPlaceholder(root, "Masukan Kata Kunci", "black", textvariable=v1)
        user_entry.config(font=("Montserrat", 15, 'italic'), bd=0, bg="#F2F2F2")
        user_entry.place(x=370, y=439, anchor=CENTER, height=60, width=600)

        ## Adding Buttons
        # test_button = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, height=1, activebackground="#6A8BFF",
        #                    font=("poppins", 20, 'bold'), text='Pengujian Sistem',
        #                   padx=10, pady=10, command=testing)
        # test_button.place(relx=0.235, rely=0.5, anchor=CENTER)
        cari_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                      font=("Montserrat", 16, 'bold'),
                      text="Cari Data", command=self.search_query, padx=8, pady=8)
        cari_button.place(x=807, y=439, anchor=CENTER, height=60, width=200)

        quit = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                      font=("Montserrat", 16, 'bold'),
                      text="Kembali", command=root.destroy, padx=8, pady=8)
        quit.place(x=170, y=530, anchor=CENTER, height=60, width=200)

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

    def input(self):
        global fname

    ## Playing the last recorded

    def search_query(self):
        st = time.time()
        global v1
        alpha_value = 0.005 #0.005
        raw_query = v1.get()
        print(raw_query)
        alpha_value = 0.005 #0.005
        result_vsm = runn(raw_query)
        result_pi = runn2(raw_query)

        print('result vsm: ', result_vsm)
        print('result pi : ', result_pi)

        result_namevsm = []
        result_bobotvsm = []

        for i in result_vsm:
            result_namevsm.append(i[0])
            result_bobotvsm.append(i[1])

        print(result_namevsm)
        print(result_bobotvsm)

        print(len(result_namevsm))
        print(len(result_pi))


        result_irisanname = []
        result_irisanbobot = []

        for i in range(len(result_namevsm)):
            for j in range(len(result_pi)):
                if result_namevsm[i] == result_pi[j]:
                    #result_irisanname.append([result_namevsm[i], result_bobotvsm[i]])
                    result_irisanname.append(result_namevsm[i])
                    result_irisanbobot.append(result_bobotvsm[i])
                    if len(result_irisanname) == 10:
                        break
        et = time.time()
        elapsed_time = et - st
        print(result_irisanname)
        print(result_irisanbobot)
        # print(result_irisanname.sort())

        final_result(result_irisanname, result_irisanbobot, raw_query, elapsed_time)


    # def train(self):
    #     global v1
    #     traine(v1.get())

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from auth import *
import sys

sys.setrecursionlimit(9000)

fname = ''



class Auth:
    def __init__(self):
        root = Toplevel()
        root.title("Login")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("1366x768")  # ("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image

        image = Image.open(r'bgg/loginbgnew.png')
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
        user_entry = self.EntryWithPlaceholder(root, "Masukan Username", "black", textvariable=v1)
        user_entry.config(font=("Montserrat", 13, 'italic'), bd=0, bg="#F2F2F2")
        user_entry.place(x=1043, y=265, anchor=CENTER, height=40, width=330)
        global v2
        v2 = StringVar()
        user_entry = self.EntryWithPlaceholder(root, "Masukan Password", "black", textvariable=v2)
        user_entry.config(font=("Montserrat", 13, 'italic'), bd=0, bg="#F2F2F2")
        user_entry.place(x=1043, y=335, anchor=CENTER, height=40, width=330)

        ## Adding Buttons
        # test_button = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, height=1, activebackground="#6A8BFF",
        #                    font=("poppins", 20, 'bold'), text='Pengujian Sistem',
        #                   padx=10, pady=10, command=testing)
        # test_button.place(relx=0.235, rely=0.5, anchor=CENTER)
        login_button = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                      font=("Montserrat", 14, 'bold'),
                      text="Login", command=self.user_auth, padx=8, pady=8)
        login_button.place(x=943, y=389, anchor=CENTER, height=45, width=130)

        quit = Button(root, bg="#4090A9", fg="#F2F2F2", bd=0, activebackground="#75B9CE",
                      font=("Montserrat", 14, 'bold'),
                      text="Kembali", command=root.destroy, padx=8, pady=8)
        quit.place(x=1093, y=389, anchor=CENTER, height=45, width=130)

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

    ## User Auth
    def user_auth(self):
        auth(v1.get(), v2.get())
    # def input(self):
    #     global fname
    #     global v1, v2, v3
    #     try:
    #         fname = testr(str(v1.get()), float(v2.get()))
    #     except:
    #         fname = testr(v1.get())
    #
    # ## Playing the last recorded
    #
    # def search_query(self):
    #     global fname
    #     play_audio(fname)
    #
    # # def train(self):
    # #     global v1
    # #     traine(v1.get())

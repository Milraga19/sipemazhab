import pathlib
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from cekdata import *

from PIL import Image, ImageTk
import shutil
from docx2pdf import convert
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from parse_func import *

import time
import sys
import glob
import os

def info(message, title="Pemberitahuan"):
    root = Tk()
    root.iconify()
    showinfo(title, message, parent=root)
    root.destroy()

sys.setrecursionlimit(9000)

fname = ''


def cek_data():
    Cek_data()

class Add_data:
    def __init__(self):
        root = Toplevel()
        root.title("Kelola Data")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("1366x768")  # ("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image

        image = Image.open(r'bgg/cekdatabgnew.png')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)


        tambah_button = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, activebackground="#6A8BFF",
                      font=("Montserrat", 16, 'bold'),
                      text="Tambah Data", command=Add_data, padx=8, pady=8)
        tambah_button.place(relx=0.09, rely=0.3, anchor=CENTER, height=50, width=200)

        cek_button = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, activebackground="#6A8BFF",
                               font=("Montserrat", 16, 'bold'),
                               text="Cek Data", command=cek_data, padx=8, pady=8)
        cek_button.place(relx=0.09, rely=0.4, anchor=CENTER, height=50, width=200)

        quit = Button(root, bg="#6A8BFF", fg="#F2F2F2", bd=0, activebackground="#6A8BFF",
                      font=("Montserrat", 16, 'bold'),
                      text="Log Out", command=root.destroy, padx=8, pady=8)
        quit.place(relx=0.09, rely=0.5, anchor=CENTER, height=50, width=200)

        input_button = Button(root, text="Input", bg="#6A8BFF", fg="#F2F2F2", bd=0, font=("Montserrat", 15, 'bold'),
                            command=self.input)
        input_button.place(relx=0.662, rely=0.287, anchor=W, width=150, height=50)

        conv_button = Button(root, text="Convert", bg="#6A8BFF", fg="#F2F2F2", bd=0, font=("Montserrat", 15, 'bold'),
                             command=self.conv)
        conv_button.place(relx=0.662, rely=0.4, anchor=W, width=150, height=50)

        train_button = Button(root, text="Buat Inverted Index", bg="#6A8BFF", fg="#F2F2F2", bd=0, font=("Montserrat", 10, 'bold'), command=self.train)
        train_button.place(relx=0.662, rely=0.513, anchor=W, width=150, height=50)

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

    def input(self):
        window = Toplevel()
        window.wm_attributes('-topmost', 1)
        window.withdraw()
        folder_path = StringVar()
        folder_selected = filedialog.askopenfilenames(parent=window)
        folder_path.set(folder_selected)
        folder = folder_path.get()
        tuple_path = eval(folder)
        path_list = list(tuple_path)
        print(path_list)
        for i in range(len(path_list)):
            folder_path = path_list[i]
            print(folder_path)
            shutil.copy2(path_list[i], "idle_path")
            print(path_list[i])
        print("complete")
        info('Sukses Menginput Dokumen')

    def conv(self):
        file_paths = glob.glob("D:\Yoga Punya\\tugas\SEMESTER 7\STKI\\testfile\idle_path" + "\\*")
        dest_file_dir_path = r"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\idle_path"

        count_pdf_path = r"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\data_pdf"

        # print(doc_paths)
        for file_path in file_paths:
            file_name = file_path.split("""\\""")[-1]
            print(file_name)
            f_name, f_ext = os.path.splitext(file_name)

            if f_ext == '.docx':
                doc_paths = glob.glob("D:\Yoga Punya\\tugas\SEMESTER 7\STKI\\testfile\idle_path" + "\\*.docx")
                dest_doc_dir_path = r"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\idle_path"
                for doc_path in doc_paths:
                    count = len([name for name in os.listdir(count_pdf_path) if
                                 os.path.isfile(os.path.join(count_pdf_path, name))])
                    count2 = count
                    filename = str(count + 1)
                    print(filename)
                    # doc_dest_full_path = dest_doc_dir_path + """\\""" + doc_name
                    convert(doc_path, dest_doc_dir_path + "\\" + filename + ".pdf")
                    shutil.copy2(dest_doc_dir_path + "\\" + filename + ".pdf", "data_pdf")
                break
            else:
                pdf_paths = glob.glob("D:\Yoga Punya\\tugas\SEMESTER 7\STKI\\testfile\idle_path" + "\\*.pdf")
                dest_pdf_dir_path = r"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\idle_path"
                for pdf_path in pdf_paths:
                    count = len([name for name in os.listdir(count_pdf_path) if
                                 os.path.isfile(os.path.join(count_pdf_path, name))])
                    count2 = count
                    filename = str(count2 + 1)
                    print(filename)
                    os.rename(pdf_path, dest_pdf_dir_path + "\\" + filename + ".pdf")
                    shutil.copy2(dest_pdf_dir_path + "\\" + filename + ".pdf", "data_pdf")
                break

        txt_paths = glob.glob("D:\Yoga Punya\\tugas\SEMESTER 7\STKI\\testfile\idle_path" +"\\*.pdf")
        dest_txt_dir_path = r"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\data_txt"
        for txt_path in txt_paths:
            filename = txt_path.split("""\\""")[-1]
            f_name, f_ext = os.path.splitext(filename)
            txt_dest_full_path = dest_txt_dir_path + """\\""" + f_name + ".txt"
            print(txt_dest_full_path)
            output_string = StringIO()
            with open(txt_path, 'rb') as in_file:
                parser = PDFParser(in_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)

            # print(output_string.getvalue())
            with open(txt_dest_full_path, 'x', encoding='utf-8') as f:
                f.write(output_string.getvalue())
        dest_doc_delete_path = r"D:\Yoga Punya\tugas\SEMESTER 7\STKI\testfile\idle_path\\"
        for doc_name in os.listdir(dest_file_dir_path):
            file = dest_doc_delete_path + doc_name
            print(file)
            if os.path.isfile(file):
                os.remove(file)
        info('Sukses Mengkonversi Dokumen')



    def train(self):
        st = time.time()
        parse()
        et = time.time()
        elapsed_time = et - st
        info('Sukses Membuat Inverted Index\n Estimasi waktu %2.5f detik' %(elapsed_time))


from flask import Blueprint, render_template, request, redirect, url_for
import time

from website.src.testlogin import *
from website.src.search_func import *


views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')


@views.route('/result', methods=['GET','POST'])
def show_result():
    if request.method == 'POST':
        queries = request.form.get('query')
        print(queries)
        st = time.time()
        # global v1
        alpha_value = 0.005  # 0.005
        raw_query = queries
        print(raw_query)
        alpha_value = 0.005  # 0.005
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
                    # result_irisanname.append([result_namevsm[i], result_bobotvsm[i]])
                    result_irisanname.append(result_namevsm[i])
                    result_irisanbobot.append(result_bobotvsm[i])
                    if len(result_irisanname) == 10:
                        break
        et = time.time()
        elapsed_time = et - st
        print(result_irisanname)
        print(result_irisanbobot)
        jumlah = len(result_irisanbobot)

        # print(result_irisanname.sort())

        query_entry=queries
        names = result_irisanname
        bobot = result_irisanbobot
    # global query
        return render_template('result.html', names=names, bobot=bobot, result=query_entry, total=jumlah, zip=zip, int=int,display_judul=display_judul, display_text=display_text, openfile=lambda x,y:openfile, openbook=lambda x:openbook)

def display_judul(doc):
    filename = 'website\src\data_txt\%d.txt' % (doc)
    f = open(filename, "r", encoding="UTF8").readlines(100)
    # print(f)
    # f[2] = f[2].replace("\n", "...")
    # new_f = (''.join(f))
    new_f = f[0], f[1]
    # print(f)
    new_f2 = (''.join(new_f))

    return new_f2

def display_text(doc,queries):
    cari = list(queries.split())
    with open('website\src\data_txt\%d.txt' % (doc), 'r+') as f:
        for line in f:
            for i in range(len(cari)):
                if cari[i] in line:
                    global a
                    a = line.split("\n")
                    a[1] = a[1].replace('', '...')
                    break
                else:
                    continue
                i += 1
    new_a = (''.join(a))
    return new_a

@views.route('/file/<name>/<queries>')
def openfile(name,queries):
    import fitz

    ## READ IN PDF
    doc = fitz.open("website\src\data_pdf\%s.pdf" % (name))
    print(doc)

    for page in doc:
        ### SEARCH
        text = list(queries.split(" "))
        text_instances = [page.search_for(text) for text in text]

        ### HIGHLIGHT
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.update()

    ### OUTPUT
    doc.save("website\src\output.pdf", garbage=4, deflate=True, clean=True)
    os.startfile('website\src\output.pdf')
    return redirect(url_for('views.home'))

@views.route('/book/<name>')
def openbook(name):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import pyautogui
    import pydirectinput
    from pynput.keyboard import Key, Controller
    import time

    filename = 'website\src\data_txt\%s.txt' % (name)
    f = open(filename, "r", encoding="UTF8").readlines(100)
    # print(f)
    # f[0] = f[0].replace("   ", "")
    # new_f = (''.join(f))
    new_f = f[0].strip().lower()
    new_f = list(new_f.split(" "))

    # set chromodriver.exe path
    chrome_opt = Options()
    chrome_opt.add_experimental_option("detach", True)
    PATH = 'website\chromedriver.exe'

    web = webdriver.Chrome(PATH, chrome_options=chrome_opt)
    web.get('https://drive.google.com/file/d/1cSSLbB6kasxZRbQHx6LDvzacGYGGFK_F/view')
    # web.get('https://www.dropbox.com/s/bd2ne9roiqbyj9f/Terjemah%20Fiqih%204%20Madzhab%20Jilid%201_compressed.pdf?dl=0')
    web.maximize_window()

    keyboard = Controller()

    time.sleep(10)
    # pydirectinput.click(x=1171, y=278)
    pyautogui.scroll(-100)
    # pydirectinput.click(x=1780, y=931)
    pyautogui.scroll(-100)
    # pydirectinput.click(x=1171, y=278)
    time.sleep(10)

    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite('a')
    pyautogui.press('backspace')
    for i in range(len(new_f)):
        pyautogui.typewrite(new_f[i])
        if i < len(new_f):
            pyautogui.typewrite(" ")

    time.sleep(5)
    time.sleep(5)

    pyautogui.press('backspace')
    pyautogui.typewrite(' ')
    pyautogui.press('backspace')

    time.sleep(5)
    time.sleep(5)

    pyautogui.press('backspace')
    pyautogui.typewrite(' ')
    pyautogui.press('backspace')
    # pyautogui.typewrite(new_f)
    # pyautogui.press('tab')
    pyautogui.hotkey('Return')
    # pydirectinput.click(x=1797, y=229)
    return redirect(url_for('views.home'))
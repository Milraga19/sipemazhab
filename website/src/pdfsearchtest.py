from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
#set chromodriver.exe path
PATH = 'E:\Yoga Punya\\tugas\chromedriver.exe'

web = webdriver.Chrome(PATH)
web.get('file:///E:/Yoga%20Punya/tugas/Bahan%20Final%20Battle/Buku%20Ar-Risalah/Terjemah%20Fiqih%204%20Madzhab%20Jilid%201.pdf')
web.maximize_window()

time.sleep(10)

pyautogui.scroll(-100)

time.sleep(5)

pyautogui.scroll(-100)

time.sleep(5)

pyautogui.scroll(-100)

time.sleep(10)

pyautogui.hotkey('ctrl','f')
pyautogui.typewrite('Hal-hal yang Membuat Mandi Meniadi Disunnahkan Atau Dianjurkan')
pyautogui.hotkey('Return')


import json
import os
import re
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters

options = Options()

driver = webdriver.Firefox(options=options,
                           executable_path="/Users/admin/PycharmProjects/uploadVideo/firefoxdriver/geckodriver_2")

API_TOKEN = '6047302451:AAH_Hm7NiUgpHiWsWz0eGIH77UtHSSF7Q2E'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def json_load(file_name):
    with open(file_name, 'r') as file:
        links = json.load(file)
        return links


def json_write(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))


url = 'https://anekdotov.net/anekdot/arc/today.html'
url = 'http://anekdotov.net/arc/230517.html'

driver.get(url=url)
file_an = '../anekdoty.json'


# everyday = json_load(file_an)


# def add_anekdot():
#     date = driver.current_url.replace('https://anekdotov.net/anekdot/arc/', '').replace('.html', '')
#     anekdoty = driver.find_elements(By.CLASS_NAME, 'anekdot')
#     everyday[date] = {}
#     for position, ane in enumerate(anekdoty):
#         everyday[date][position] = {}
#         everyday[date][position]['text'] = ane.text
#         everyday[date][position]['lenght'] = len(ane.text)


def find_next_page():
    all_a = driver.find_elements(By.TAG_NAME, 'a')
    for a in all_a:
        if a.text == '>>':
            a.click()
        # if a.text == 'Д А Л Е Е!':
        #     a.click()


def find_next_page2():
    next_page = driver.find_element(By.XPATH, '/html/body/center/div/div[1]/form/table[16]/tbody/tr/td[3]/a')

    # / html / body / center / div / div[1] / table[25] / tbody / tr / td[4] / a
    next_page.click()


driver.get(url=url)


def start_parse():
    everyday = json_load(file_an)
    date = driver.current_url.replace('https://anekdotov.net/anekdot/arc/', '').replace('.html', '')
    anekdoty = driver.find_elements(By.CLASS_NAME, 'anekdot')
    everyday[date] = {}
    for position, ane in enumerate(anekdoty, 1):
        everyday[date][position] = {}
        everyday[date][position]['text'] = ane.text
        everyday[date][position]['lenght'] = len(ane.text)
        regexp_ane = '.н.кд.т.в\.n.t'
        everyday[date][position]['text'] = re.sub(regexp_ane, '', everyday[date][position]['text']).strip()
        # everyday[date][position]['text'].replace('aнeкдoтов.nеt', '')

    time.sleep(0.5)
    json_write(file_an, everyday)
    find_next_page()
    # find_next_page2()
    time.sleep(0.5)

for _ in range(10):
    start_parse()
    print('OK')
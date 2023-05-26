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


url = 'http://anekdotov.net/arc/today.html'
# url = 'http://anekdotov.net/arc/230517.html'
url = 'http://anekdotov.net/arc/211115.html'

driver.get(url=url)
file_every_day = 'anekdoty_everyday'
file_all = '2anekdoty.json'
last_id = 0


def find_next_page3():
    nav_bar = driver.find_element(By.CLASS_NAME, 'pagenavibig')
    links_bar = nav_bar.find_elements(By.TAG_NAME, 'a')
    links_bar[3].click()


driver.get(url=url)


def start_parse(l_id=last_id):
    date = driver.current_url.replace('http://anekdotov.net/arc/', '').replace('.html', '')
    year = str(date[0]) + str(date[1])
    file_name = file_every_day + year + '.json'
    if os.path.exists(file_name):
        everyday = json_load(file_name)
    else:
        everyday = {}
    anekdoty = driver.find_elements(By.CLASS_NAME, 'anekdot')
    everyday[date] = {}
    for position, ane in enumerate(anekdoty, 1):
        everyday[date][position] = {}

        everyday[date][position]['id'] = 'id' + str(l_id)
        everyday[date][position]['text'] = ane.text
        everyday[date][position]['lenght'] = len(ane.text)
        everyday[date][position]['publish'] = False
        everyday[date][position]['interesting'] = ''
        everyday[date][position]['view'] = ''
        regexp_ane = '.н.кд.т.в\.n.t'
        everyday[date][position]['text'] = re.sub(regexp_ane, '', everyday[date][position]['text']).strip()
        l_id += 1
    time.sleep(0.5)
    json_write(file_name, everyday)
    find_next_page3()
    time.sleep(0.5)
    return


# for _ in range(10):
#     start_parse()
#     print('OK')

while True:
    start_parse()
    print('OK')



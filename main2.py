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


def json_load(file_name):
    with open(file_name, 'r') as file:
        links = json.load(file)
        return links


def json_write(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))


anekdot_ru = 'anekdot_ru.json'
# url = 'https://www.anekdot.ru/last/anekdot/'
last_url_json = json_load('last_url.json')
url = last_url_json['url']


def find_next_page3():
    find_pagination = driver.find_element(By.CLASS_NAME, 'voteresult')
    links_a = find_pagination.find_element(By.TAG_NAME, 'a')
    links_a.click()


driver.get(url=url)


def start_parse():
    if os.path.exists(anekdot_ru):
        anekdots = json_load(anekdot_ru)
    else:
        anekdots = {}

    time.sleep(1)
    find_anekdots = driver.find_elements(By.CLASS_NAME, 'topicbox')
    for f_a in find_anekdots:
        if f_a.get_attribute('data-id'):
            id_an = f_a.get_attribute('data-id')
            anekdots[id_an] = f_a.find_element(By.CLASS_NAME, 'text').text

    json_write(anekdot_ru, anekdots)
    find_next_page3()
    print(len(anekdots))
    last_url = {
        'url' : driver.current_url
    }

    json_write('last_url.json', last_url)


while True:
    start_parse()
    print('OK')



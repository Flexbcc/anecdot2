import json
import os
import re
import time
import random
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters



API_TOKEN = '6251782445:AAEU-LAm8Vhcm35JkS8QYpftY1vcjsXLa40'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def json_load(file_name):
    with open(file_name, 'r') as file:
        links = json.load(file)
        return links


anekdot_ru = json_load('anekdot_ru.json')


def get_random_ane():
    my_text = anekdot_ru[random.choice(list(anekdot_ru))]
    print(my_text)
    return my_text


async def send_mes(another_text):
    my_text = get_random_ane()
    print(another_text)
    await bot.send_message(chat_id='-1001950212840', text=my_text + '\n\n '+ str(another_text) + '\n #hashtag #hashtag2 '
                                                                     '\n для связи с админимстатором напишите @ane123k5dots')

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
# -1001950212840
# scheduler.add_job(send_mes, "interval", seconds=5, args=['\n каждый день с 9 до 23 каждые 5 минут'
#                                                                      '\n #hashtag #hashtag2 '
#                                                                      '\n для связи с админимстатором напишите @ane123k5dots '])
# scheduler.add_job(send_mes, "interval", seconds=120, args=['\n каждые 120 секунд'])
# scheduler.add_job(send_mes, "interval", hours=1, args=['\n каждый час'])
scheduler.add_job(send_mes, 'cron', hour='12', minute='11', args=['каждый день в 12-11'])
scheduler.add_job(send_mes, 'cron', hour='8-22', minute='22', args=['каждый день с 8 до 22 в 22 минуты'])
scheduler.add_job(send_mes, 'cron', hour='8-22', minute='33', args=['каждый день с 8 до 22 в 33 минуты'])
scheduler.add_job(send_mes, 'cron', hour='8-22', minute='46', args=['каждый день с 8 до 22 в 44 минуты'])
scheduler.add_job(send_mes, 'cron', hour='8-22', minute='57', args=['каждый день с 8 до 22 в 57 минут'])
scheduler.add_job(send_mes, 'cron', hour='8-22', minute='*/5', args=['каждый день с 8 до 22 каждые 5 минут'])
# scheduler.add_job(send_mes, 'cron', hour='0', second='*/10', args=['начинается пиздец'])
scheduler.add_job(send_mes, 'cron', hour='9', second='*/15', args=['каждый день в 9 часов каждые 15 секунд, начинается пиздец'])


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)

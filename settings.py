import json
import os
import re
import time
import random
import time
import aiogram
import codecs
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand
from aiogram.dispatcher import filters


def json_load(file_name):
    with open(file_name, 'r') as file:
        links = json.load(file)
        return links


def json_write(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))


scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
SETTING = json_load('settings.json')
API_TOKEN = SETTING['API_TOKEN']
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

admins_id = [
    1, 324, 45252, 498480465, 424234,  896325021
]

anekdot_ru = json_load('anekdot_ru.json')

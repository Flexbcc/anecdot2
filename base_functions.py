from settings import *


async def send_mes(channel):
    my_text = get_random_anekdots()
    if channel == 'base':
        # Title: АНЕКДОТЫ I РАССМЕШНИЛО
        channel_id = '-1001903707923'
    else:
        # testanekdots
        # -1001646369830
        channel_id = '-1001950212840'
    await bot.send_message(chat_id=channel_id,
                           text=f'{my_text} \n{get_hashtag_text()}\n\n {get_about_text()}',
                           parse_mode="HTML",
                           disable_web_page_preview=True)
    # parse_mode="HTML", disable_web_page_preview=True,  reply_markup=urlkb ,  reply_markup=keyboard)


def clear_view():
    data = json_load('publish_anekdots.json')
    data['view'] = []
    json_write('publish_anekdots.json', data)
    print(f'View data is clear')


def clear_publish():
    data = json_load('publish_anekdots.json')
    data['publish'] = []
    json_write('publish_anekdots.json', data)
    print(f'Publish data is clear')


def clear_interesting():
    data = json_load('publish_anekdots.json')
    data['interesting'] = []
    json_write('publish_anekdots.json', data)
    print(f'Interesting data is clear')


def check_counts(if_print=False):
    publish_data = json_load('publish_anekdots.json')
    anekdots_data = json_load('anekdot_ru.json')
    len_anekdots = len(anekdots_data)
    len_view = len(publish_data['view'])
    len_publish = len(publish_data['publish'])
    len_interesting = len(publish_data['interesting'])
    if if_print:
        print(f'anekdots - {len_anekdots}\n'
              f'view - {len_view}\n'
              f'publish - {len_publish}\n'
              f'interesting - {len_interesting}\n')
    return len_anekdots, len_view, len_publish, len_interesting


count_info = check_counts()
print(SETTING)


def get_about_text_link():
    asd = json_load('settings.json')
    return asd['about_text_link']


def set_about_text_link(new_text):
    SETTING['about_text_link'] = new_text
    json_write('settings.json', SETTING)


def get_about_text_text():
    asd = json_load('settings.json')
    return asd['about_text_text']


def set_about_text_text(new_text):
    SETTING['about_text_text'] = new_text
    json_write('settings.json', SETTING)


def get_hashtag_text():
    asd = json_load('settings.json')
    return_text = ''
    if len(asd['hashtag_text']) <= 1:
        return_text = asd['hashtag_text']
    else:
        for hashtags in asd['hashtag_text']:
            return_text += f'{hashtags} ,'
    return return_text[:-1]


def add_hashtag_text(new_hashtag):
    if new_hashtag not in SETTING['hashtag_text']:
        SETTING['hashtag_text'].append(f'#{new_hashtag}')
    else:
        pass
    json_write('settings.json', SETTING)


def del_hashtag_text(hashtag):
    if hashtag in SETTING['hashtag_text']:
        SETTING['hashtag_text'].pop(hashtag)
    else:
        pass
    json_write('settings.json', SETTING)


def get_random_anekdots():
    not_unique = json_load('publish_anekdots.json')
    random_id = random.choice(list(anekdot_ru))
    # publish = not_unique['publish']
    view = not_unique['view']
    # interesting = not_unique['interesting']

    if random_id not in view:
        view.append(random_id)
    # elif random_id not in publish:
    #     publish.append(random_id)
    # elif random_id not in interesting:
    #     interesting.append(random_id)
    else:
        get_random_anekdots()

    json_write('publish_anekdots.json', not_unique)
    my_text = anekdot_ru[random.choice(list(anekdot_ru))]
    return my_text


def get_about_text():
    # asd = json_load('settings.json')
    if get_about_text_link() == '':
        about_text = f'{get_about_text_text()}'
    else:
        about_text = f'<a href="{get_about_text_link()}"> {get_about_text_text()} </a>'
    return about_text


def add_timer(text):
    asd = json_load('settings.json')
    timers = asd['timers']
    timer_settings = text.split(' ')
    timers[timer_settings[0]] = {
        "type": timer_settings[1],
        "hours": timer_settings[2],
        "minutes": timer_settings[3],
        "args": timer_settings[4]
    }
    json_write('settings.json', asd)


def del_timer(name_timer):
    asd = json_load('settings.json')
    if name_timer in asd['timers']:
        asd['timers'].pop(name_timer)
        json_write('settings.json', asd)
    else:
        print('Not found')
        pass


def get_timers():
    asd = json_load('settings.json')
    timers = asd['timers']
    ret_text = ''
    for timer, settings in timers.items():
        ret_text += timer + ' , '
    return ret_text[:-2]


def start_all_timers():
    asd = json_load('settings.json')
    timers = asd['timers']
    for timer, settings in timers.items():
        print(timer)
        print(settings)
        # print(settings['type'], settings['hours'], settings['minutes'], settings['args'])
        scheduler.add_job(send_mes, settings['type'], hour=settings['hours'], minute=settings['minutes'],
                          args=[settings['args']], id=timer)


def add_job_timers(timer_name):
    asd = json_load('settings.json')
    timers = asd['timers']
    settings = timers[timer_name]
    scheduler.add_job(send_mes, settings['type'], hour=settings['hours'], minute=settings['minutes'],
                      args=[settings['args']], id=timer_name)


@dp.message_handler(commands=['get_timers'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"список таймеров - {get_timers()}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['add_timer'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    arg = msg.text.replace('/add_timer', '').strip()
    if mes_us_id in admins_id:
        timer_settings = arg.split(' ')
        add_timer(arg)
        add_job_timers(timer_settings[0])
        my_text = f"Вы добавили таймер - {arg}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['del_timer'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    arg = msg.text.replace('/del_timer', '').strip()
    if mes_us_id in admins_id:
        del_timer(arg)
        my_text = f"Вы удалили таймер - {arg}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)
    scheduler.remove_job(arg)


@dp.message_handler(commands=['get_about_text_link'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Ссылка в описании - {get_about_text_link()}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['get_about_text_text'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Текст в описании - {get_about_text_text()}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['get_hashtag_text'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Хештеги в описании - {get_hashtag_text()}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['get_about_text'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Весь текст в описании - {get_about_text()}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['set_about_text_link'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    arg = msg.text.replace('/set_about_text_link', '').strip()
    if mes_us_id in admins_id:
        set_about_text_link(arg)
        my_text = f"Вы изменили ссылку в описании - {arg}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['set_about_text_text'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    arg = msg.text.replace('/set_about_text_text', '').strip()
    if mes_us_id in admins_id:
        set_about_text_text(arg)
        my_text = f"Вы изменили текст в описании - {arg}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['add_hashtag_text'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    arg = msg.text.replace('/add_hashtag_text', '').strip()
    if mes_us_id in admins_id:
        add_hashtag_text(arg)
        my_text = f"Вы добавили хештег - {arg}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['del_hashtag_text'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    arg = msg.text.replace('/del_hashtag_text', '').strip()
    if mes_us_id in admins_id:
        del_hashtag_text(arg)
        my_text = f"Вы изменили ссылку в описании - {arg}"
    else:
        my_text = 'fuck ***'
    await msg.reply(text=my_text)


@dp.message_handler(commands=['get_count_anekdots'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Количество анекдотов - {count_info[0]}"
    else:
        my_text = 'fuck ***'

    await msg.reply(text=my_text)


@dp.message_handler(commands=['get_count_view'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Количество показанных анекдотов - {count_info[1]}"
    else:
        my_text = 'fuck ***'

    await msg.reply(text=my_text)


@dp.message_handler(commands=['get_count_publish'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Количество опубликованных анекдотов - {count_info[2]}"
    else:
        my_text = 'fuck ***'

    await msg.reply(text=my_text)


@dp.message_handler(commands=['get_count_interesting'])
async def command(msg: types.Message):
    mes_us_id = msg.from_user.id
    if mes_us_id in admins_id:
        my_text = f"Количество интересных анекдотов - {count_info[3]}"
    else:
        my_text = 'fuck ***'

    await msg.reply(text=my_text)


async def on_startup(dispatcher: aiogram.Dispatcher) -> None:
    await bot.set_my_commands([
        aiogram.types.BotCommand("get_timers", "Показать таймеры"),
        aiogram.types.BotCommand("add_timer",  "Добавить таймер 5 арг (Название cron часы минуты base1"),
        aiogram.types.BotCommand("del_timer",  "Удалить таймер с именем"),
        aiogram.types.BotCommand("get_about_text_link",  "Получить ссылку в описании"),
        aiogram.types.BotCommand("get_about_text_text",  "Получать текст в описании"),
        aiogram.types.BotCommand("get_hashtag_text",  "Получить список хэштегов"),
        aiogram.types.BotCommand("get_about_text",  "Получить полный текст описания"),
        aiogram.types.BotCommand("set_about_text_link",  "Новая ссылка в описании"),
        aiogram.types.BotCommand("set_about_text_text",  "Новый текст в описании"),
        aiogram.types.BotCommand("add_hashtag_text",  "Добавить хэштег"),
        aiogram.types.BotCommand("del_hashtag_text",  "Удалить хэштег"),
        aiogram.types.BotCommand("get_count_anekdots",  "Получить список анекдотов"),
        aiogram.types.BotCommand("get_count_view",  "Получить кол-во показанных анекдотов"),
        aiogram.types.BotCommand("get_count_publish",  "Получить кол-во опубликованных анекдотов"),
        aiogram.types.BotCommand("get_count_interesting",  "Получить кол-во избранных анекдотов")
    ])
from base_functions import *

# kb = [
#     [
#         types.KeyboardButton(text="Сможешь повторить это?"),
#         types.KeyboardButton(text="А это?")
#     ],
# ]
# keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#
# urlkb = InlineKeyboardMarkup(row_width=2)
# urlButton = InlineKeyboardButton(text='👍')
# urlButton2 = InlineKeyboardButton(text='👎')
# urlkb.add(urlButton, urlButton2)


# scheduler.add_job(send_mes, "interval", seconds=10, args=['base1'])
# scheduler.add_job(send_mes, 'cron', hour='8-22', minute='49', args=['base1'])
# scheduler.add_job(send_mes, 'cron', hour='8-22', minute='*/5', args=['base1'])
# set_default_commands(dp)
start_all_timers()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
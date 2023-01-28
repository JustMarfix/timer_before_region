#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import Config
from time import time

import threading
import telebot
import os

bot = telebot.TeleBot(Config.token)
final_time = Config.final_time
cid = Config.cid
mid = Config.mid

def main():
    threading.Timer(60.0, main).start()
    now = int(time())
    days = (final_time - now) // 86400
    hours = (final_time - now - (days*86400)) // 3600
    minutes = (final_time - now - (days*86400) - (hours*3600)) // 60
    if minutes < 0 or days < 0 or hours < 0:
        bot.edit_message_text('Регион начался!', cid, mid)
        os._exit(0)
    text = f'До регионального этапа ВсОШ по Праву осталось {days} дн. {hours} ч. {minutes} мин.'
    try:
        bot.edit_message_text(text, cid, mid)
    except telebot.apihelper.ApiTelegramException as error1:
        try:
            bot.send_message(cid, text)
            bot.edit_message_text(text, cid, mid)
        except BaseException as error2:
            print('Ошибка:', error2)
main()
#!/usr/bin/env python
# -*- coding:utf-8
import bot
from config import api_list
from utils.tools import add_log, regex
import threading

class sid(threading.Thread):
	def __init__(self, type_bot):
		threading.Thread.__init__(self)
		self.type_bot = type_bot

	def run(self):
		try:
			add_log(self.type_bot, 'Start Bot ' + self.type_bot, True, True)
			bot.start_bot(type_bot)
		except Exception as err:
			add_log(err, 'Stop Bot', True, True)
			exit()

for type_bot in api_list:
	sid(type_bot).start()

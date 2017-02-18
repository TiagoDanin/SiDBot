#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.database import *
from utils.help import *
from utils.tools import add_log, regex
from config import plugins_list, debug, api_list
from objectjson import ObjectJSON
from importlib import import_module as import_plugin
import threading

add_log('Bot....',
		'Bot Run!', True)

class run_plugin(threading.Thread):
	def __init__(self, msg_text, chat_id, bot_type):
		threading.Thread.__init__(self)
		self.msg_text    = msg_text
		self.chat_id 	 = chat_id
		self.bot_type    = bot_type
		if debug:
			#I need some privacy here ;-;
			self.debug = True

	def run(self):
			for plugin in plugins_list:
				res = import_plugin('plugins.{plugin}'.format(plugin=plugin))
				for patt in res.patterns:
					matches = regex(patt, self.msg_text)
					if matches:
						if self.debug:
							add_log('{cmd} - {plugin}: {text} '.format(
										cmd = patt,
										plugin = plugin,
										text = self.msg_text
										),
										'[TRIGGER]'
									)
							res.run(self,  matches.group(1), matches)

def start_plugin(msg_text, chat_id, bot_type):
	try:
		run_plugin(msg_text, chat_id, bot_type).start()
	except Exception as error_load:
		add_log('Failed run_plugin: {}'.format(error_load) , 'Error in bot!', True)

def start_bot():
	if 'cli' in api_list:
		while True:
			msg_text = input('> /')
			print('Say: /' + msg_text)
			start_plugin(
				msg_text = '/' + msg_text,
				chat_id = 12345,
				bot_type = 'cli'
			)
try:
	start_bot()
except Exception as error:
	add_log('B O T: {}'.format(error), 'Stop Bot', True)
	exit()

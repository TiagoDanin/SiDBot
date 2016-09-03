#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.database import *
from utils.help import *
from utils.methods import getMe, getUpdates
from utils.utils import add_log, regex
from config import plugins_list, debug
from objectjson import ObjectJSON
from importlib import import_module as import_plugin
import threading

class info():
	info, _ = getMe()
	if info == None:
		add_log('No is possible obtain data','Error in bot!')
		exit()
	username = info.result.username
	first_name = info.result.first_name
	id = info.result.id

add_log('Bot {}\tID {}\tUSERNAME {}'.format(info.first_name, info.id, info.username),
		'Bot Run!')

update_id = 0
if r.get('{}:update_id'.format(hash)):
	update_id = r.get('{}:update_id'.format(hash))

class run_plugin(threading.Thread):
	def __init__(self, msg, type):
		threading.Thread.__init__(self)
		self.update = msg
		self.update = ObjectJSON(msg)
		self.bot = info
		self.type = type
		if debug:
			#I need some privacy here ;-;
			self.debug = True
			add_log(self.update, 'Update')

	def run(self):
			for plugin in plugins_list:
				res = import_plugin('plugins.{plugin}'.format(plugin=plugin))
				for patt in res.patterns:
					if self.type == 'message':
						if self.update.message.text:
							matches = regex(patt, self.update.message.text)
							if matches:
								res.run(self, self.update.message, matches)
					elif self.type == 'inline':
						if self.update.inline_query.query:
							matches = regex(patt, self.update.inline_query.query)
							if matches:
								res.run_inline(self, self.update.inline_query, matches)

def start_plugin(msg, type):
	if msg:
		try:
			run_plugin(msg, type).start()
		except Exception as error_load:
			add_log('Failed run_plugin: {}'.format(error_load) , 'Error in bot!')

def start_bot(get_updates):
	update_id = 0
	while get_updates:
		_, result = getUpdates(offset=update_id + 1)
		if result:
			for msg in result['result']:
				update_id = msg['update_id']
				if 'message' in msg:
					start_plugin(msg, 'message')
				elif 'inline_query' in msg:
					start_plugin(msg, 'inline')
		else:
			add_log('Failed getUpdates', 'Error in bot!')

try:
	start_bot(True)
except Exception as error:
	add_log('B O T: {}'.format(error), 'Stop Bot')
	r.set('{}:update_id'.format(hash), update_id)
	exit()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from config import plugins_list, debug, send_falid_plugin, dev_mode
from config import admins, defaut_lang, port, host
from utils.database import incr_database
from utils.languages import get_user_lang
from utils.methods import sendFalid
from utils.tools import add_log, regex
from objectjson import ObjectJSON
from flask import Flask, request, make_response
from importlib import import_module as import_plugin
from json import dumps as json_dumps
import threading

class run_plugin(threading.Thread):
	def __init__(self, msg_text, chat_id, bot_type):
		threading.Thread.__init__(self)
		self.msg_text    = msg_text
		self.chat_id 	 = chat_id
		self.bot_type    = bot_type
		self.user_lang   = defaut_lang
		if debug:
			#I need some privacy here ;-;
			self.debug = debug
		if send_falid_plugin:
			self.send_falid_plugin = send_falid_plugin
		if dev_mode:
			self.dev_mode = dev_mode

	def run(self):
		for plugin in plugins_list:
			res = import_plugin('plugins.{plugin}'.format(plugin=plugin))
			for patt in res.patterns:
				matches = regex(patt, self.msg_text)
				if matches:
					if 'admin_plugin' in res.config:
						if res.config['admin_plugin']:
							if self.chat_id == admins[self.bot_type]:
								add_log('Safe user' + str(self.chat_id),
									'Admin Plugin'
								)
					self.plugin = plugin
					self.matches = matches
					self.trigger = patt

					# Status
					incr_database(table='status', name='allbot_usage')
					incr_database(table='status',
						name=str('bot_usage:' + self.bot_type)
					)
					incr_database(table='status',
						name=str('plugin_usage:' + plugin)
					)
					if self.bot_type == 'telegram-inline':
						incr_database(table='status',
							name=str('inline_usage')
						)

					# Get user_lang
					self.user_lang = get_user_lang(self)

					if self.debug:
						add_log('{cmd} - {plugin}: {text} '.format(
								cmd = patt,
								plugin = plugin,
								text = self.msg_text
							),
							'[TRIGGER]'
						)

					if self.dev_mode:
						res.run(self,  matches.group(1), matches)
					else:
						try:
							res.run(self,  matches.group(1), matches)
						except Exception as err:
							add_log('Failed run_plugin: {}'.format(err),
								'Error in bot!',
								True, True
							)
							if self.send_falid_plugin:
								sendFalid(self, title='BOT', reason='generic')

def start_plugin(msg_text, chat_id, bot_type):
	try:
		run_plugin(msg_text, chat_id, bot_type).start()
	except Exception as err:
		add_log('Failed start_plugin: {}'.format(err),
			'Error in bot!',
			True, True
		)

def start_bot(type_bot):
	while True:
		#CLI
		if type_bot == 'cli':
			msg_text = input('Say: /')
			start_plugin(
				msg_text = str('/' + msg_text),
				chat_id = 123456,
				bot_type = 'cli'
			)
		#Telegram
		if type_bot == 'telegram':
			update_id = 0
			_, result = getUpdates(offset=update_id + 1)
			if result:
				for msg in result['result']:
					update_id = msg['update_id']
					if 'message' in msg:
						if 'text' in msg['message']:
							if 'chat' in msg['message']:
								start_plugin(
									msg_text = str(msg.message.text),
									chat_id = int(msg.message.chat.id),
									bot_type = 'telegram'
								)
					if 'inline_query' in msg:
						if 'query' in msg['inline_query']:
							if 'id' in msg['inline_query']:
								start_plugin(
									msg_text = str('/' + msg.inline_query.query),
									chat_id = int(msg.inline_query.id),
									bot_type = 'telegram-inline'
								)
				else:
					add_log('Failed getUpdates', 'Error in bot!')
		#Telegram-Classic
		if type_bot == 'telegram-classic':
			update_id = 0
			_, result = getUpdates(offset=update_id + 1)
			if result:
				for msg in result['result']:
					update_id = msg['update_id']
					if 'message' in msg:
						if 'text' in msg['message']:
							if 'chat' in msg['message']:
								start_plugin(
									msg_text = str(msg.message.text),
									chat_id = int(msg.message.chat.id),
									bot_type = 'telegram'
								)
				else:
					add_log('Failed getUpdates', 'Error in bot!')
		#Telegram-Inline
		if type_bot == 'telegram-inline':
			update_id = 0
			_, result = getUpdates(offset=update_id + 1)
			if result:
				for msg in result['result']:
					update_id = msg['update_id']
					if 'inline_query' in msg:
						if 'query' in msg['inline_query']:
							if 'id' in msg['inline_query']:
								start_plugin(
									msg_text = str('/' + msg.inline_query.query),
									chat_id = int(msg.inline_query.id),
									bot_type = 'telegram-inline'
								)
				else:
					add_log('Failed getUpdates', 'Error in bot!')
		# Web API
		# SOON
		if type_bot == 'web-api':
			app = Flask(__name__)
			def index():
				start_plugin(
					msg_text = str('/' + request.args['msg_text']),
					chat_id = int(request.args['chat_id']),
					bot_type = 'web-api'
				)
				res = json_dumps({'tiago': 'danin'}, indent=4)
				r = make_response(res)
				r.headers['Content-Type'] = 'application/json'
				return r

			app.add_url_rule('/', 'Index', index, methods=['GET'])
			app.run(host=host, port=port, debug=False)

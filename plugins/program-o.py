name = "SiD IA - Program-o"
patterns = [
	"^sid (.*)$"
]
description = ""

from utils.methods import sendMessage
from utils.request import request_json

def api(msg, text):
	url_api = 'http://api.program-o.com/v2/chatbot/'
	params = {}
	params['bot_id'] = '6'
	params['say'] = text
	params['convo_id'] = 'sidbot_user{}'.format(msg.chat.id)
	params['format'] = 'json'
	res_obj, res_str = request_json(url=url_api, params=params)
	if not res_str:
		return 'Error'
	return res_obj.botsay

def run(self, msg, matches):
	text = matches.group(1)
	sendMessage(chat_id=msg.chat.id,
				text=api(msg, text))
	return

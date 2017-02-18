name = 'smile'
patterns = [
	'^[!/]smile (.*)$'
]
description = 'Returns a text with smileys'

from utils.methods import sendMessage, sendInline
from utils.inline import make_inline

def new_text(text):
	return text.replace(' ', ' :) ')

def run(self, msg, matches, input):
	text = new_text(matches.group(1))
	sendMessage(chat_id=msg.chat.id, text=text, parse_mode='Markdown')
	return

def run_inline(self, msg, matches, input):
	text = new_text(matches.group(1))
	pic = 'http://icons.iconarchive.com/icons/iconsmind/outline/128/Smile-icon.png'
	sendInline(inline_query_id=msg.id,
				results=make_inline('article',
					title='Smile!',
					just=True,
					message_text=text,
					description=text,
					thumb_url=pic
				),
				cache_time=3)
	return

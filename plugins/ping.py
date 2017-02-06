name = "Ping!"
patterns = [
	"^[!/](ping)$"
]
description = "🏓 Ping Pong"

from utils.methods import sendMessage, sendInline
from utils.inline import make_inline

text = '*Pong* 🎾'
def run(self, msg, matches, input):
	sendMessage(chat_id=msg.chat.id, text=text, parse_mode='Markdown')
	return

def run_inline(self, msg, matches, input):
	pic = "http://icons.iconarchive.com/icons/iconsmind/outline/128/Ping-Pong-icon.png"
	sendInline(inline_query_id=msg.id,
				results=make_inline('article',
					title='Ping!',
					just=True,
					message_text=text,
					description='P.O.N.G',
					parse_mode='Markdown',
					thumb_url=pic
				),
				cache_time=3)
	return

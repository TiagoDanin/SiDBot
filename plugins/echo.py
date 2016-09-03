name = "Echo"
patterns = [
	"^[!/]echo (.*)$"
]
description = "Will return text"

from utils.methods import sendMessage, sendInline
from utils.inline import make_inline

def run(self, msg, matches):
	sendMessage(chat_id=msg.chat.id, text=matches.group(1))
	return

def run_inline(self, msg, matches):
	pic = "http://icons.iconarchive.com/icons/icons8/windows-8/128/Security-Voice-Recognition-Scan-icon.png"
	markdown_help = "*bold text*    _italic text_\n[text](URL)    ```code block```"
	html_help = "<b>bold text</b>    <i>italic text</i>\n<a href=\'\'URL\'\'>text</a>\n<pre>pre>code block</pre>"
	block = '['
	block = block + make_inline('article', title='Custom Markdown', message_text=matches.group(1),
			description=markdown_help, parse_mode='Markdown', thumb_url=pic)
	block = block + ',' + make_inline('article', title='Custom HTML', message_text=matches.group(1),
			description=html_help, parse_mode='HTML', thumb_url=pic)
	block = block + ',' + make_inline('article', title='Without Formatting', message_text=matches.group(1),
			description='without formatting...', thumb_url=pic)
	block = block + ']'
	sendInline(inline_query_id=msg.id,
				results=block,
				cache_time=3)
	return

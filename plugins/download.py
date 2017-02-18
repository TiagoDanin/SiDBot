name = 'Download'
patterns = [
	'^[!/]download (.*)$'
]
description = 'Download a file'

from utils.methods import sendMessage, sendFile
from utils.inline import make_inline

def run(self, msg, matches, input):
	file_url = matches.group(1)
	sendMessage(chat_id=msg.chat.id, text='📥 Downloading...')
	res, _ = sendFile(chat_id=msg.chat.id, file=file_url, name=file_url)
	if res.ok == False:
		sendMessage(chat_id=msg.chat.id, text='❌ Error: Invalid URL')
	return

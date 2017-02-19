name = 'Ping!'
patterns = [
	'^[!/](ping)$'
]
description = '🏓 Ping Pong'
usage = ''
config = {}

from utils.methods import sendText

def run(self, input, matches):
	sendText(self, title='Ping', text='Pong 🎾')
	return

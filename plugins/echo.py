name = 'Echo'
patterns = [
	'^[!/]echo (.*)$'
]
description = 'Will return text'
usage = ''
config = {}

from utils.methods import sendText

def run(self, input, matches):
	sendText(self, title='Echo', text=input)
	return

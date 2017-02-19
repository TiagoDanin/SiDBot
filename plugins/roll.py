name = 'Roll'
patterns = [
	'^[!/](roll)$',
	'^[!/]roll ((([\d]*)))$',
	'^[!/]roll (([\d]*) ([\d]*))$'
]
description = 'Return a random number'
usage = ''
config = {}

from utils.methods import sendText
import random

def run(self, input, matches):
	if input == 'roll':
		n = random.randrange(1, 7)
	elif matches.group(2) != matches.group(3):
		if matches.group(2) < matches.group(3):
			n = random.randrange(int(matches.group(2)), int(matches.group(3)))
		else:
			n = random.randrange(int(matches.group(3)), int(matches.group(2)))
	elif matches.group(2) == matches.group(3):
		n = random.randrange(1, int(matches.group(2)))
	sendText(self, title='Roll', text=n)
	return

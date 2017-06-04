name = 'Status'
patterns = [
	'^[!/](status)$',
]
description = 'Returns status.'
usage = ''
config = {
	'admin_plugin': True
}

from utils.methods import sendResults
from utils.database import *
from config import plugins_list
import dataset

def get_status(input):
	db = dataset.connect('sqlite:///db' + hash)
	table = db['status']
	r = table.find_one(name=input)
	if r == None:
		return str(input + ': 0')
	i = r['value']
	output = str(input + ': ' + str(i))
	return output

def run(self, input, matches):
	if input == 'status':
		t = []
		t.append(get_status('allbot_usage'))
		t.append(get_status('bot_usage:' + self.bot_type))
		t.append(get_status('inline_usage'))
		for v in plugins_list:
			t.append(get_status('plugin_usage:' + v))

		sendResults(self, title='Status', text=False, results=t)
		return

name = 'help'
patterns = [
	'^[!/](help)$',
	'^[!/]help (.*)$'
]
description = 'Get info about plugins'
usage = ''
config = {}

from utils.methods import sendList, sendAbout, sendFalid
from config import plugins_list
from importlib import import_module as import_plugin

def run(self, input, matches):
	if input == 'help':
		t = []
		for plugin in plugins_list:
			p = import_plugin('plugins.{}'.format(plugin))
			t.append(p.name)
		sendList(self, title='List of Plugins', text=False, results=t)
		return
	else:
		if input in plugins_list:
			p = import_plugin('plugins.{}'.format(input))
			if 'hide' in p.config:
				if p.config['hide']:
					sendFalid(self, title='Plugin', reason='results')
					return

			sendAbout(self,
				title=p.name,
				about=p.description,
				more_about=p.usage,
				title_url=False,
				url=False,
				img=False
			)
			return
		else:
			sendFalid(self, title='Plugin', reason='results')
			return
	return

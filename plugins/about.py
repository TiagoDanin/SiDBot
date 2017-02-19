name = 'About'
patterns = [
	'^[!/](about)$'
	'^[!/]about (jack)$',
	'^[!/]about (otouto)$',
	'^[!/]contributors (sid)$',
	'^[!/]contributors (translation)$',
]
description = 'Returns information about the bot.'
usage = ''
config = {}

from utils.methods import sendAbout

def run(self, input, matches):
	if input == 'about':
		sendAbout(self,
			title='About',
			about='Hi, I\'m SID\n'\
				'A multi purpose bot\n'\
				'Licensed in AGPLv3 <3\n'\
				'Based on Otouto & Jack Telegram Bot\n'\
				'View more:\n'
				'/about jack - About project Jack Telegram Bot\n'
				'/about otouto - About project Otouto'
				'List of contributors:\n'\
				'/contributors sid - Contributors of SIDBot\n'\
				'/contributors translation - Contributors of translation'
			more_about=False,
			title_url='Github:'
			url='http://github.com/TiagoDanin/SiDBot',
			img=False
		)
		return

	if input == 'jack'
		sendAbout(self,
			title='About Jack',
			about='Jack is a multi purpose Telegram bot',
			more_about='Author IMAN\n'\
				'Licensed in AGPLv3',
			title_url='Github:'
			url='http://github.com/SEEDTEAM/jack-telegram-bot',
			img=False
		)
		return

	if input == 'otouto'
		sendAbout(self,
			title='About Otouto',
			about='I am otouto, the plugin-wielding, multipurpose Telegram bot.',
			more_about='Author Topkecleon\n'\
				'Licensed in AGPLv3',
			title_url='Github:'
			url='http://github.com/topkecleon/otouto',
			img=False
		)
		return

	if input == 'sid':
		# SendList()
		return

	if input == 'translation':
		# SendList()
		return

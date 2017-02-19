from api.cli import show_terminal, check_debug_in_cli
import PythonColorize as ct
#from api.telegram import *

def sendText(self, title=None, text=None):
	# *Title*
	# text
	if not title or not text:
		if self.dev_mode:
			print('sendText: Missing "title" or "text" in {}'.format(self.plugin))
		return False

	if self.bot_type == 'cli':
		check_debug_in_cli(self)
		show_terminal('{bold}{title}{rest}\n{text}'.format(
						bold=ct.colors.lg_bold_white,
						title=title,
						rest=ct.colors.nocolor,
						text=text
							)
						)
		return True
	return False

def sendAbout(self, title=None, about=None, more_about=None, title_url=None, url=None, img=None):
	# [hack_img](img)
	# *Title*
	# about
	# _more_about_
	# title_url: url

	if not title or not about:
		if self.dev_mode:
			print('sendAbout: Missing "title" or "about" in {}'.format(self.plugin))
		return False
	if not more_about:
		more_about = ''
	else:
		more_about = str(more_about + '\n')

	if self.bot_type == 'cli':
		if img:
			img_text = str('IMG URL:' + img + '\n')
		else:
			img_text = ''

		if title_url and url:
			text_url = str(title_url + ': ' + url)
		elif url:
			text_url = str('URL: ' + url)
		else:
			text_url = ''

		check_debug_in_cli(self)
		show_terminal('{img_text}'\
			'{bold}{title}{rest}\n'\
			'{about}\n'\
			'{dark}{more_about}{rest}'\
			'{text_url}'\
			.format(
				img_text=img_text,
				bold=ct.colors.lg_bold_white,
				title=title,
				rest=ct.colors.nocolor,
				about=about,
				dark=ct.colors.lg_dark_magenta,
				more_about=more_about,
				text_url=text_url
			)
		)
	return False

def sendResult(self, title=None, text=None, results=None):
	# *Title*
	# *Results for* _text
	# for in ... (.)results[1] ... results[2]
	return False

def sendList(self, title=None, text=None, results=None):
	# *Title*
	# _text_
	# for in ... (n=0, n+1)results[1] ... results[2]
	if not title or not results:
		if self.dev_mode:
			print('sendList: Missing "title" or "results" in {}'.format(self.plugin))
		return False
	if not text:
		text = ''
	else:
		text = str(text + '\n')

	if self.bot_type == 'cli':
		n = 0
		list_text = ''
		for v in results:
			n += 1
			list_text += str(n) + '. ' + str(v) + '\n'
		check_debug_in_cli(self)
		show_terminal('{bold}{title}{rest}\n{text}{list}'.format(
				bold=ct.colors.lg_bold_white,
				title=title,
				rest=ct.colors.nocolor,
				text=text,
				list=list_text
			)
		)
		return True
	return False

def sendFalid(self, title=None, reason=None):
	# *title*
	# reason
	if not title or not reason:
		if self.dev_mode:
			print('sendFalid: Missing "title" or "reason" in {}'.format(self.plugin))
		return False

	text = 'An unexpected error occurred.'
	if reason == 'generic':
		text = 'An unexpected error occurred.'
	if reason == 'connection':
		text = 'Connection error.'
	if reason == 'results':
		text = 'No results found.'
	if reason == 'argument':
		text = 'Invalid argument.'
	if reason == 'syntax':
		text = 'Invalid syntax.'

	if self.bot_type == 'cli':
		check_debug_in_cli(self)
		show_terminal('{bold_w}{title}{rest}\n{bold_r}{text}{rest}'.format(
				bold_w=ct.colors.lg_bold_white,
				bold_r=ct.colors.lg_bold_red,
				rest=ct.colors.nocolor,
				title=title,
				text=text,
			)
		)
		return True
	return False

def sendLog(title=None, date=None, log=None):
	# *Title*
	# Date: date
	# ```
	# log
	# ```
	return False

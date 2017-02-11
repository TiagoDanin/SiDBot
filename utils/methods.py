from api.cli import show_terminal
import PythonColorize as ct
#from api.telegram import *

def sendText(self, title=None, text=None):
	# *Title*
	# text
	if self.bot_type == 'cli':
		show_terminal('{bold}{title}{rest}\n{text}'.format(
						bold=ct.colors.lg_bold_white,
						title=title,
						rest=ct.colors.nocolor,
						text=text
							)
						)
	return True

def sendAbout(self, title=None, text=None, about=None, url=None, img=None):
	# [hack_img](img)
	# *Title*
	# text
	# _about_
	# Url: url
	return True

def sendResult(self, title=None, text=None, results=None):
	# *Title*
	# *Results for* _text
	# for in ... (.)results[1] ... results[2]
	return True

def sendList(self, title=None, text=None, results=None):
	# *Title*
	# _text_
	# for in ... (n=0, n+1)results[1] ... results[2]
	return True

def sendLog(title=None, date=None, log=None):
	# *Title*
	# Date: date
	# ```
	# log
	# ```
	return True

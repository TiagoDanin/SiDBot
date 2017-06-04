from config import print_log
from utils.methods import *
from PythonColorize import *
import datetime
import re

def add_log(f=None, type_=None, save=None, send=None):
	time = datetime.datetime.now()
	if save:
		file = open('tmp/{}-log.txt'.format(type_), 'a')
		text = '{time} -- {type_}\n{f}\n\n'.format(time=time,
													type_=type_,
													f=f)
		file.write(text)
		file.close()

	if send:
		sendLog(title='#LOG {type_}'.format(type_=type_), date=time, log=f)

	if print_log:
		type_  = colors.lg_red + type_ + colors.nocolor
		time   = colors.lg_blue + str(time) + colors.nocolor
		f      = colors.green + str(f) + colors.nocolor
		div    = colors.lg_yellow + '----' + colors.nocolor
		text   = '\n{div}\t{type_}\t{div}\t{time}\t{div}\n{f}\n\n'.format(div=div,
																	type_=type_,
																	time=time,
																	f=f)
		print(text)

	return

def regex(pattern=None, string=None):
	capt = re.match(pattern, string)
	if bool(capt):
		return capt
	return None

from config import *
from PythonColorize import *
import datetime
import re

def add_log(f=None, type_=None):
	time  = datetime.datetime.now()
	type_ = colors.lg_red + type_ + colors.nocolor
	time  = colors.lg_blue + str(time) + colors.nocolor
	f     = colors.green + str(f) + colors.nocolor
	div   = colors.lg_yellow + '----' + colors.nocolor
	text  = '\n{div}\t{type_}\t{div}\t{time}\t{div}\n{f}\n\n'.format(div=div,
																	type_=type_,
																	time=time,
																	f=f)
	if print_log:
		print(text)
	file = open('tmp/log.text', 'a')
	file.write(text)
	file.close()
	return

def regex(pattern=None, string=None):
	capt = re.match(pattern, string)
	if bool(capt):
		return capt
	return None

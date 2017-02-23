from config import defaut_lang
from utils.database import db, hash
from utils.tools import add_log
from importlib import import_module as import_lang
import dataset

def get_user_lang(self):
	db = dataset.connect('sqlite:///database:' + hash)
	table = db['user:' + str(self.bot_type) + str(self.chat_id)]
	r = table.find_one(info='lang')
	if r == None:
		table.insert(dict(info='lang', value=defaut_lang))
		return defaut_lang

	return r['value']

def update_user_lang(self, new_lag):
	if get_user_lang(self) == new_lag:
		return new_lag
	else:
		db = dataset.connect('sqlite:///database:' + hash)
		table = db['user:' + str(self.bot_type) + str(self.chat_id)]
		a = dict(info='lang', value=new_lag)
		table.update(a, ['info'])
		return new_lag

def new_str(self, text):
	f = open('languages/{lang}.py'.format(lang=self.user_lang), 'r')
	new_text = ''
	for s in f.readlines():
		if s.replace('\n', '') == '}':
			text = text.replace('\'', '\\\'')
			text = text.replace('"', '\\"')
			new_text += '	\'{text}\': \'{text}\',\n'.format(text=text) + str('}')
		else:
			new_text += '{}'.format(s)

	f = open('languages/{lang}.py'.format(lang=self.user_lang), 'w')
	f.write(new_text)
	f.close()
	add_log('New text in lang-{}'.format(self.user_lang), 'Languages')
	return

def get_str(self, text):
	l = import_lang('languages.{}'.format(self.user_lang))
	if text in l.lang:
		return l.lang[text]
	else:
		new_str(self, text)
		return text

_ = get_str

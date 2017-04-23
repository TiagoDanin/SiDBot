from config import db_id
import dataset

hash = 'bot{}'.format(str(db_id))

db = dataset.connect('sqlite:///database' + hash)

# table = db['bot']
#table.insert(dict(name='John Doe', age=37))
#table.insert(dict(name='Jane Doe', age=34, gender='female'))

#john = table.find_one(name='John Doe')

def incr_database(table=None, name=None):
	db = dataset.connect('sqlite:///database:' + hash)
	if table and name:
		table = db[table]
		r = table.find_one(name=name)
		if r == None:
			table.insert(dict(name=name, value=0))
			r = table.find_one(name=name)

		new = r['value'] + 1
		a = dict(name=name, value=new)
		table.update(a, ['name'])
		return new
	return Falseacpi -V

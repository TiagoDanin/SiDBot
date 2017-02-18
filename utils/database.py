import dataset
from config import db_id

hash = 'bot:{}'.format(str(db_id))

db = dataset.connect('sqlite:///:memory:')

# table = db['bot']
#table.insert(dict(name='John Doe', age=37))
#table.insert(dict(name='Jane Doe', age=34, gender='female'))

#john = table.find_one(name='John Doe')

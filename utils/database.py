from utils.utils import add_log
import dataset
import redis

hash = 'bot:'
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

db = dataset.connect('sqlite:///:memory:')

# table = db['bot']
#table.insert(dict(name='John Doe', age=37))
#table.insert(dict(name='Jane Doe', age=34, gender='female'))

#john = table.find_one(name='John Doe')

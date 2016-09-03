from utils.utils import add_log
import redis

hash = 'bot:'
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
if not r.ping():
	add_log('Redis not is run', 'Error in database!')
	exit()

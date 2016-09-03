from objectjson import ObjectJSON
from utils.utils import add_log
import config
import requests

timeout = config.timeout
token = config.token
telegram = 'https://api.telegram.org/bot{token}/'.format(token=token)

def request_url(url, type=None, params=None, headers=None, auth=None, files=None, setime=None):
	time = timeout
	if setime:
		time = setime
	try:
		data = requests.get(url, params=params, headers=headers, auth=auth, files=files, timeout=time)
	except:
		return None

	if data.status_code == 200:
		return data
	else:
		add_log('Error in request! {}\n{}\n\n{}'.format(url, params, data.text), 'Request')
	return None

def request_file():
	#SOON
	return

def request_json(url, params=None, headers=None, auth=None, files=None, setime=None):
	data = request_url(url=url, params=params, headers=headers, auth=auth, files=files, timeout=time)
	if data == None:
		return None, None
	json_str = data.json()
	json_obj = ObjectJSON(json_str)
	return json_obj, json_str

def request_telgram(method, query=None, file_=None):
	url = telegram + method
	data = request_url(url, params=query, files=file_, setime=timeout)
	if data == None:
		return None, None
	json_str = data.json()
	json_obj = ObjectJSON(json_str)
	return json_obj, json_str

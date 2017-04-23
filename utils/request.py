from config import timeout, telegram_bot_token, telegram_or_pwrtelegram
from utils.tools import add_log
import requests
from objectjson import ObjectJSON

telegram = 'https://api.telegram.org/bot{token}/'.format(token=telegram_bot_token)
pwrtelegram = 'https://api.pwrtelegram.xyz/bot{token}/'.format(token=telegram_bot_token) #- http://pwrtelegram.xyz/ -#
if telegram_or_pwrtelegram == 'pwrtelegram':
	telegram = pwrtelegram

def request_url(url, type=None, params=None, headers=None, auth=None, files=None, setime=None):
	time = timeout
	if setime:
		time = setime
	try:
		data = requests.get(url, params=params, headers=headers, auth=auth, files=files, timeout=time)
	except Exception as error:
		add_log(str(error) + '\nURL: ' + str(url), 'Request-Except', True)
		return False

	if data.status_code == 200:
		return data
	else:
		add_log('Error in request! {}\n{}\n\n{}'.format(url, params, data.text), 'Request', True)
	return False

def request_post(url, params=None, headers=None, data=None):
        data = requests.post(url, params=params, headers=headers, data=data)
        if data.status_code != 200:
		#add_log(data.status_code)
		#add_log(data.text)
		add_log("OK")
		return
		
def request_file():
	#SOON
	return

def request_json(url, params=None, headers=None, auth=None, files=None, setime=None):
	data = request_url(url=url, params=params, headers=headers, auth=auth, files=files, setime=setime)
	if data == False:
		return False, False
	try:
		json_str = data.json()
	except:
		return False, False
	json_obj = ObjectJSON(json_str)
	return json_obj, json_str

def request_telgram(method, query=None, file_=None):
	url = telegram + method
	data = request_url(url, params=query, files=file_, setime=timeout)
	if data == False:
		return False, False
	try:
		json_str = data.json()
	except:
		return False, False
	json_obj = ObjectJSON(json_str)
	return json_obj, json_str

def request_pwrtelgram(method, query=None, file_=None):
	url = pwrtelegram + method
	data = request_url(url, params=query, files=file_, setime=timeout)
	if data == False:
		return False, False
	try:
		json_str = data.json()
	except:
		return False, False
	json_obj = ObjectJSON(json_str)
	return json_obj, json_str

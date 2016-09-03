name = "Calculator"
patterns = [
	"^[!/]calc (.*)$"
]
description = "Return the result"

from utils.methods import sendMessage, sendInline
from utils.request import request_url
from utils.inline import make_inline

def api(calc):
	api = 'http://api.mathjs.org/v1/'
	params = {}
	params['expr'] = calc
	res = request_url(url=api, params=params)
	if not res:
		return 'Error'
	return res.text

def run(self, msg, matches):
	sendMessage(chat_id=msg.chat.id, text='*Result:* `{}`'.format(api(matches.group(1))),
				parse_mode='Markdown')
	return

def run_inline(self, msg, matches):
	pic = "http://icons.iconarchive.com/icons/martz90/circle/128/calculator-icon.png"
	cal = matches.group(1)
	result = api(cal)
	res = '*Result:* {} = {}'.format(cal, result)
	sendInline(inline_query_id=msg.id,
				results=make_inline('article', title='Result!', just=True,
					message_text=res, description=res,
					parse_mode='Markdown', thumb_url=pic),
				cache_time=3)
	return

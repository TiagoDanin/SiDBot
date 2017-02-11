import json
import random

#Inline for Telegram
def make_keyboard(text=None, url=None, callback_data=None, switch_inline_query=None):
	keyborad = {}
	if text:
		keyborad['text'] = text
	if url:
		keyborad['url'] = url
	if callback_data:
		keyborad['callback_data'] = callback_data
	if switch_inline_query:
		keyborad['switch_inline_query'] = switch_inline_query
	return json.dumps(keyborad)

def make_inline(type=None, id=None, title=None, message_text=None, just=None, reply_markup=None,
				parse_mode=None, disable_web_page_preview=None, inline_keyboard=None, url=None,
				hide_url=None, description=None,
				thumb_url=None, thumb_width=None, thumb_height=None):
	inline = {}
	if id:
		inline['id'] = id
	else:
		inline['id'] = str(random.randint(1, 800))
	if type:
		inline['type'] = type
	if title:
		inline['title'] = title
	if message_text:
		inline['message_text'] = message_text
	if parse_mode:
		inline['parse_mode'] = parse_mode
	if disable_web_page_preview:
		inline['disable_web_page_preview'] = disable_web_page_preview
	if reply_markup:
		inline['reply_markup'] = reply_markup
	if inline_keyboard:
		inline['inline_keyboard'] = inline_keyboard
	if url:
		inline['url'] = url
	if hide_url:
		inline['hide_url'] = url
	if description:
		inline['description'] = description
	if thumb_url:
		inline['thumb_url'] = thumb_url
	if thumb_width:
		inline['thumb_width'] = thumb_width
	if thumb_height:
		inline['thumb_height'] = thumb_height
	if just:
		return '[' + json.dumps(inline) + ']'
	return json.dumps(inline)

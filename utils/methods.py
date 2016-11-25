from utils.request import request_telgram, request_pwrtelgram
import json

def check_querys(chat_id=None, text=None, parse_mode=None, disable_web_page_preview=None,
				disable_notification=None, reply_to_message_id=None, reply_markup=None,
				inline_keyboard=None, photo=None, caption=None, audio=None, duration=None,
				performer=None, title=None, document=None, sticker=None, video=None,
				width=None,height=None, voice=None, latitude=None, longitude=None,
				address=None, foursquare_id=None, phone_number=None,
				first_name=None, last_name=None, action=None, user_id=None, offset=None,
				limit=None, file__id=None, callback_querys_id=None, show_alert=None,
				inline_message_id=None, message_id=None, timeout=None, from_chat_id=None,
				inline_query_id=None, results=None, cache_time=None, is_personal=None,
				next_offset=None, switch_pm_text=None, switch_pm_parameter=None, file=None,
				name=None):

	querys = {}
	file_ = {}
	if chat_id:
		querys['chat_id'] = chat_id
	if text:
		querys['text'] = text
	if parse_mode:
		querys['parse_mode'] = parse_mode
	if disable_web_page_preview:
		querys['disable_web_page_preview'] = disable_web_page_preview
	if disable_notification:
		querys['disable_notification'] = disable_notification
	if reply_to_message_id:
		querys['reply_to_message_id'] = reply_to_message_id
	if reply_markup:
		querys['reply_markup'] = reply_markup
	if inline_keyboard:
		querys['reply_markup'] = '{"inline_keyboard":' + inline_keyboard + '}'
	if from_chat_id:
		querys['from_chat_id'] = from_chat_id
	if photo:
		file_['photo'] = photo
	if caption:
		querys['caption'] = caption
	if audio:
		file_['audio'] = audio
	if duration:
		querys['duration'] = duration
	if performer:
		querys['performer'] = performer
	if title:
		querys['title'] = title
	if document:
		file_['document'] = document
	if sticker:
		file_['sticker'] = sticker
	if video:
		file_['video'] = video
	if width:
		querys['width'] = width
	if height:
		querys['height'] = height
	if voice:
		file_['voice'] = voice
	if latitude:
		querys['latitude'] = latitude
	if longitude:
		querys['longitude'] = longitude
	if address:
		querys['address'] = address
	if foursquare_id:
		querys['foursquare_id'] = foursquare_id
	if phone_number:
		querys['phone_number'] = phone_number
	if first_name:
		querys['first_name'] = first_name
	if last_name:
		querys['last_name'] = last_name
	if action:
		querys['action'] = action
	if user_id:
		querys['user_id'] = user_id
	if offset:
		querys['offset'] = offset
	if limit:
		querys['limit'] = limit
	if file__id:
		querys['file__id'] = file__id
	if callback_querys_id:
		querys['callback_querys_id'] = callback_querys_id
	if show_alert:
		querys['show_alert'] = show_alert
	if inline_message_id:
		querys['inline_message_id'] = inline_message_id
	if message_id:
		querys['message_id'] = message_id
	if timeout:
		querys['timeout'] = timeout
	if name:
		querys['name'] = name
	if file:
		querys['file'] = file
	#Inline
	if inline_query_id:
		querys['inline_query_id'] = inline_query_id
	if results:
		querys['results'] = results
	if cache_time:
		querys['cache_time'] = cache_time
	if is_personal:
		querys['is_personal'] = is_personal
	if next_offset:
		querys['next_offset'] = next_offset
	if switch_pm_text:
		querys['switch_pm_text'] = switch_pm_text
	if switch_pm_parameter:
		querys['switch_pm_parameter'] = switch_pm_parameter
	return querys, file_

#https://core.telegram.org/bots/api/#available-methods
def getMe():
	return request_telgram('getMe')

def getUpdates(offset=None, limit=None, timeout=None):
	querys, file_ = check_querys(offset=offset,
							limit=limit,
							timeout=timeout)
	return request_telgram('getUpdates', querys, file_)

def sendMessage(chat_id=None, text=None, parse_mode=None, disable_web_page_preview=None,
				disable_notification=None, reply_to_message_id=None, reply_markup=None,
				inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							text=text,
							parse_mode=parse_mode,
							disable_web_page_preview=disable_web_page_preview,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendMessage', querys, file_)

def forwardMessage(chat_id=None, from_chat_id=None, disable_notification=None,
					message_id=None):

	querys, file_ = check_querys(chat_id=chat_id,
							from_chat_id=from_chat_id,
							disable_notification=disable_notification,
							message_id=message_id)
	return request_telgram('forwardMessage', querys, file_)

def sendPhoto(chat_id=None, photo=None, caption=None, disable_notification=None,
				reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							photo=photo,
							caption=caption,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendPhoto', querys, file_)

def sendAudio(chat_id=None, audio=None, duration=None, performer=None, title=None,
			disable_notification=None, reply_to_message_id=None, reply_markup=None,
			inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							audio=audio,
							duration=duration,
							performer=performer,
							title=title,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendAudio', querys, file_)

def sendDocument(chat_id=None, document=None, caption=None, disable_notification=None,
				reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							document=document,
							caption=caption,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendDocument', querys, file_)

def sendSticker(chat_id=None, sticker=None, disable_notification=None, reply_to_message_id=None,
				reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							sticker=sticker,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendSticker', querys, file_)


def sendVideo(chat_id=None, video=None, duration=None, width=None, height=None,
				caption=None, disable_notification=None, reply_to_message_id=None,
				reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							video=video,
							duration=duration,
							width=width,
							height=height,
							caption=caption,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendVideo', querys, file_)

def sendVoice(chat_id=None, voice=None, duration=None, disable_notification=None,
				reply_to_message_id=None, reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							voice=voice,
							duration=duration,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendVoice', querys, file_)

def sendLocation(chat_id=None, latitude=None, longitude=None, disable_notification=None,
				reply_to_message_id=None, reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							latitude=latitude,
							longitude=longitude,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendLocation', querys, file_)

def sendVenue(chat_id=None, latitude=None, longitude=None, title=None, address=None,
				foursquare_id=None, disable_notification=None, reply_markup=None,
				inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							latitude=latitude,
							longitude=longitude,
							title=title,
							address=address,
							foursquare_id=foursquare_id,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendVenue', querys, file_)

def sendContact(chat_id=None, phone_number=None, first_name=None, last_name=None,
				disable_notification=None, reply_to_message_id=None, reply_markup=None,
				inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							phone_number=phone_number,
							first_name=first_name,
							last_name=last_name,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendContact', querys, file_)

def sendChatAction(chat_id=None, action=None):

	querys, file_ = check_querys(chat_id=chat_id,
							action=action)
	return request_telgram('sendChatAction', querys, file_)

def sendFile(chat_id=None, file=None, name=None):

	querys, file_ = check_querys(chat_id=chat_id,
							file=file,
							name=name)
	return request_pwrtelgram('sendFile', querys, file_)

def getUserProfile_Photos(user_id=None, offset=None, limit=None):

	querys, file_ = check_querys(user_id=user_id,
							offset=offset,
							limit=limit)
	return request_telgram('getUserProfile_Photos', querys, file_)

def getfile_(file__id=None):

	querys, file_ = check_querys(file__id=file__id)
	return request_telgram('getfile_', querys, file_)

def kickChatMember(chat_id=None, user_id=None):

	querys, file_ = check_querys(chat_id=chat_id,
							user_id=user_id)
	return request_telgram('kickChatMember', querys, file_)

def leaveChat(chat_id=None):

	querys, file_ = check_querys(chat_id=chat_id)
	return request_telgram('leaveChat', querys, file_)

def unbanChatMember(chat_id=None, user_id=None):

	querys, file_ = check_querys(chat_id=chat_id,
							user_id=user_id)
	return request_telgram('unbanChatMember', querys, file_)

def getChat(chat_id=None):

	querys, file_ = check_querys(chat_id=chat_id)
	return request_telgram('getChat', querys, file_)

def getChatAdministrators(chat_id=None):

	querys, file_ = check_querys(chat_id=chat_id)
	return request_telgram('getChatAdministrators', querys, file_)

def getChatMembersCount(chat_id=None):

	querys, file_ = check_querys(chat_id=chat_id)
	return request_telgram('getChatMembersCount', querys, file_)

def getChatMember(chat_id=None, user_id=None):

	querys, file_ = check_querys(chat_id=chat_id,
							user_id=user_id)
	return request_telgram('getChatMember', querys, file_)

def answerInlinequerys(callback_querys_id=None, text=None, show_alert=None):

	querys, file_ = check_querys(callback_querys_id=callback_querys_id,
							text=text,
							show_alert=show_alert)
	return request_telgram('answerInlinequerys', querys, file_)

#https://core.telegram.org/bots/api/#updating-messages
def editMessageText(chat_id=None, message_id=None, inline_message_id=None, text=None,
				parse_mode=None, disable_web_page_preview=None, reply_markup=None,
				inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							message_id=message_id,
							inline_message_id=inline_message_id,
							text=text,
							parse_mode=parse_mode,
							disable_web_page_preview=disable_web_page_preview,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('editMessageText', querys, file_)

def editMessageCaption(chat_id=None, message_id=None, inline_message_id=None, caption=None,
				reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							message_id=message_id,
							inline_message_id=inline_message_id,
							caption=caption,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('editMessageCaption', querys, file_)

def editMessageReplyMarkup(chat_id=None, message_id=None, inline_message_id=None,
				reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							message_id=message_id,
							inline_message_id=inline_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('editMessageReplyMarkup', querys, file_)

#https://core.telegram.org/bots/api/#inline-mode
def sendInline(inline_query_id=None, results=None, cache_time=None, is_personal=None,
				next_offset=None, switch_pm_text=None, switch_pm_parameter=None):

	querys, file_ = check_querys(inline_query_id=inline_query_id,
							results=results,
							cache_time=cache_time,
							is_personal=is_personal,
							next_offset=next_offset,
							switch_pm_text=switch_pm_text,
							switch_pm_parameter=switch_pm_parameter)
	return request_telgram('answerInlineQuery', querys, file_)

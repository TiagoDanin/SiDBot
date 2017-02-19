#Global
timeout = 5
db_id = 12
debug = True
dev_mode = True
print_log = True
saved_log = False
send_falid_plugin = True

# Token's
telegram_bot_token = ''
telegram_or_pwrtelegram = 'pwrtelegram'

# API's
api_list = [
	'cli',
	#'telegram', #Need Test
	#'telegram-classic', #Need Test
	#'telegram-inline', #Need Test
]

admins = {
	'cli': [
		000000,
		123456
	],
	'telegram': [
		00000
	]
}

# Plugin's
plugins_list = [
	#'calculator',
	#'download',
	'echo',
	'help',
	'ping',
	#'program-o'
	'roll',
	#'smile',
	'status'
]

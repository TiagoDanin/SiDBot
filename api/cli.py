def show_terminal(text=None):
	if text:
		print('Bot SAY: ' + text)
		return True
	else:
		return False

def check_debug_in_cli(self):
	if self.debug:
		#Clean
		print('- \t - \t - \t - \t - \t - \t - \t - \t -')
		print('- \t - \t - \t - \t - \t - \t - \t - \t -')
		print('- \t - \t - \t - \t - \t - \t - \t - \t -')
	return

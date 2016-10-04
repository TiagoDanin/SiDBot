if [ "$1" = "--help" ]; then
	echo -e "
HELP CMD
--update         Sync bot with master repo
--install        Run install
--help           Prints this msg
REQUIREMENTS
--python 3.5.2
--pip 8.1.2
"

elif [ "$1" = "--update" ]; then
	git pull
elif [ "$1" = "--install" ]; then
	sudo pip install -r requirements.txt
else
	echo -e "
  ____  _ ____  ____        _
 / ___|(_)  _ \| __ )  ___ | |_
 \___ \| | | | |  _ \ / _ \| __|
  ___) | | |_| | |_) | (_) | |_
 |____/|_|____/|____/ \___/ \__| V5.2
"
	while true; do
		python bot.py "${@}"
		sleep 5s
	done
fi

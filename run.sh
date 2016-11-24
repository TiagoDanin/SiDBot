if [ "$1" = "--help" ]; then
	echo -e "
HELP CMD
--update         Sync bot with master repo
--install        Run install
--redis          Run redis in daemonize mode
REQUIREMENTS
--python 3.5.2
--pip 8.1.2
"
elif [ "$1" = "--update" ]; then
	echo "Sync..."
	git pull
elif [ "$1" = "--install" ]; then
	echo "Install libs..."
	sudo pip install -r requirements.txt
elif [ "$1" = "--redis" ]; then
	echo "Run redis in daemonize mode..."
	redis-server --daemonize yes
else
	echo -e "
  ____  _ ____  ____        _
 / ___|(_)  _ \| __ )  ___ | |_
 \___ \| | | | |  _ \ / _ \| __|
  ___) | | |_| | |_) | (_) | |_  By Tiago Danin
 |____/|_|____/|____/ \___/ \__| V5.2
"
	while true; do
		python bot.py "${@}"
		sleep 5s
	done
fi

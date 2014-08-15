#!/bin/bash
### BEGIN INIT INFO
# Provides:          upload.sh
# Required-Start:    $remote_fs $syslog $local_fs $network $time
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

 
case "$1" in
	start)
		echo "Starting example"
		# run application you want to start
		cd /home/
		sudo python data_log.py &
		sudo ./upload.sh &
	;;
	stop)
		echo "Stopping example"
		# kill application you want to stop
		killall python
	;;	
	*)
	echo "Usage: /etc/init.d/example{start|stop}"
    exit 1
    ;;
esac
 
exit 0

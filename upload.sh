while true 
do 
	sudo ./dropbox_uploader.sh delete /data/
	sudo ./dropbox_uploader.sh upload /home/data/ / 
	#sudo ./dropbox_uploader.sh download /control/logging_increment.txt /home/control/logging_increment.txt 
	sleep 300 
done

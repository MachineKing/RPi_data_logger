follow the instructions at https://github.com/andreafabrizi/Dropbox-Uploader 
to set up the dropbox account access.

place drop.sh in /etc/init.d/
run update-rc

place upload.sh, data_log.py and dropbox_uploader.sh in /home/

give all scripts root privileges with chmod 755 <script_name>

install adafruit's DHT python library for communicating with DHT11 humidity sensor from https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_DHT_Driver_Python

create a folder: /home/data/
two text files will be placed in this folder called indoor_temp.txt and humidity.txt full of data from the ds18b20 and DHT11 respectively

reboot and the programs will run


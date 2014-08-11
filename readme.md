place drop.sh in /etc/init.d/
run update-rc

place upload.sh, data_log.py and dropbox-uploader.sh in /home/

give all scripts root privileges with chmod 755 <script_name>

follow the instructions at https://github.com/andreafabrizi/Dropbox-Uploader 
to set up the dropbox account access.

install adafruits DHT python library for communicating with DHT11 humidity sensor from https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_DHT_Driver_Python


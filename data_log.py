import os, glob, time, sys, datetime, Adafruit_DHT, subprocess
ti = datetime.datetime.now()
day_prev = int(ti.strftime('%M'))


dht_sensor = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
dht_pin = 11



def read_temp_raw(): #a function that grabs the raw temperature data from the sensor
	f_1 = open(device_file, 'r')
	lines_1 = f_1.readlines()
	f_1.close()
	f_2 = open(device_file, 'r')
	lines_2 = f_2.readlines()
	f_2.close()
	return lines_1 + lines_2
 
 
def read_temp(): #a function that checks that the connection was good and strips out the temperature
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES' or lines[2].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t='), lines[3].find('t=')
	temp = float(lines[1][equals_pos[0]+2:])/1000, float(lines[3][equals_pos[1]+2:])/1000
	return temp



if __name__ == '__main__':
		
	#MAIN CODE IS HERE		
	try:
		device_folder = glob.glob('/sys/bus/w1/devices/28-000005aaf157/w1_slave')
		device_file = '/sys/bus/w1/devices/28-000005aaf157/w1_slave'
		while True:
		#=======================================================================================================================================
		#Get sensor data
		#=======================================================================================================================================
			temp = read_temp() #get the temp
			humidity, h_temp = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
						
			temp1 = str(temp[0])
			ti = datetime.datetime.now()
			time_string = ti.strftime('%d/%m/%Y-%H:%M:%S')
			day = int(ti.strftime('%M'))

			#=======================================================================================================================================
			#Store Data in text file
			#=======================================================================================================================================
			#try to open the text file, if it doesn't exist create it
			try:
				t = open("/home/data/indoor_temp.txt", "ab")
			except:
				t = open("/home/data/indoor_temp.txt", "wb")
			t.write(time_string)
			t.write(' ')
			t.write(temp1)
			t.write('\r\n')	
			t.close			
			print time_string, '   ', temp1
			if humidity is not None and h_temp is not None:
				#open text file containing DHT11 data
				try:
					DHT = open("/home/data/humidity.txt", "ab")
				except:
					DHT = open("/home/data/data/humidity.txt", "wb")
				DHT.write(time_string)
				DHT.write(' ')
				DHT.write(str(humidity))
				DHT.write('%')
				DHT.write(' ')
				DHT.write(str(h_temp))
				DHT.write('\r\n')
				DHT.close
			
				print 'temp={0:0.1f}*C Humidity={1:0.1f}%' .format(h_temp, humidity)
			else:
				print 'Failed to get humidity reading.'
			#=======================================================================================================================================
			#get logging time from dropbox
			#=======================================================================================================================================
			#=======================================================================================================================================
			time.sleep(10) #set to whatever
			ti_prev = datetime.datetime.now() 
			day_prev = int(ti_prev.strftime('%M'))
    
 
	except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
		print "\nKilling Thread..."
		print "Done.\nExiting."





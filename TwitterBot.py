from twython import Twython
import os
import datetime

CONSUMER_KEY = 'GLTiEnGQDx1ECP4vQkBaXNNVF'
CONSUMER_SECRET = 'Z6iMkx29WAVKV5IQ3Fr8l2v7k323HgZRVYzNHa44rl093UShAy'
ACCESS_KEY = '1036407906596319232-rjcWv83wII5jYkT5V1L4rWLcBLYCMD'
ACCESS_SECRET = 'wT9nultxDgKxg3kuePg58yRFXopFICr3Q7b83rNA4MSbQ'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

try:
	api.update_status(status='My current CPU temperature is '+temp+' C')
except:
	api.update_status(status= 'No change in CPU temperature. '+ str(datetime.datetime.today()) + ' is the time')
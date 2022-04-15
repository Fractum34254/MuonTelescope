import RPi.GPIO as gpio
import time

coinGPIO = 14
gpio.setmode(gpio.BCM)
gpio.setup(coinGPIO, gpio.IN)

start = time.time()
cur = time.time()
coin = 0

while cur-start < 30:
	#if round(cur-0.00001,0)!=round(cur,0):
		#print("Time: " + str(round(cur-start,2)) + "s, Coincidences: " + str(coin))
	if gpio.input(coinGPIO):
		coin += 1
	cur = time.time()
print("Coincidences found: " + str(coin))
gpio.cleanup()

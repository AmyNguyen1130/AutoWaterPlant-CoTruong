#!/usr/bin/env python
#
# Analog Input with ADC0832 chip
#
# Datasheet: http://www.ti.com/lit/ds/symlink/adc0838-n.pdf
# Part of SunFounder LCD StarterKit
# http://www.sunfounder.com/index.php?c=show&id=21&model=LCD%20Starter%20Kit
# 
import wave
import time
import os
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
file = open("Downloads/SensorData.txt", "w")
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
PIN_CLK = 18
PIN_DO  = 27
PIN_DI  = 22
PIN_CS  = 17

# set up the SPI interface pins
GPIO.setup(PIN_DI,  GPIO.OUT)
GPIO.setup(PIN_DO,  GPIO.IN)
GPIO.setup(PIN_CLK, GPIO.OUT)
GPIO.setup(PIN_CS,  GPIO.OUT)

# read SPI data from ADC8032
def getADC(channel):
	# 1. CS LOW.
        GPIO.output(PIN_CS, True)      # clear last transmission
        GPIO.output(PIN_CS, False)     # bring CS low

	# 2. Start clock
        GPIO.output(PIN_CLK, False)  # start clock low

	# 3. Input MUX address
        for i in [1,1,channel]: # start bit + mux assignment
                 if (i == 1):
                         GPIO.output(PIN_DI, True)
                 else:
                         GPIO.output(PIN_DI, False)

                 GPIO.output(PIN_CLK, True)
                 GPIO.output(PIN_CLK, False)

        # 4. read 8 ADC bits
        ad = 0
        for i in range(8):
                GPIO.output(PIN_CLK, True)
                GPIO.output(PIN_CLK, False)
                ad <<= 1 # shift bit
                if (GPIO.input(PIN_DO)):
                        ad |= 0x1 # set first bit

        # 5. reset
        GPIO.output(PIN_CS, True)

        return ad


if __name__ == "__main__":
        while True:
		adc0=getADC(0)*2
		adc1=getADC(1)*2
		moisture= 100-((adc0+adc1)*100/1020)
               	print "moisture: {} %".format(moisture)
		now = datetime.datetime.now()
		file.write("moisture soil: "+str(moisture)+" "+"time: "+str(now) + "\n")
		time.sleep(1)
		if (moisture<=55 and 5<=now.hour<=10)or(moisture<=55 and 11<=now.hour<=18):

			GPIO.setmode(GPIO.BCM)
			GPIO.setwarnings(False)
			GPIO.setup(19,GPIO.OUT)
			GPIO.output(19,GPIO.HIGH)
			time.sleep(3)
		else:
			GPIO.setup(19,GPIO.OUT)
			GPIO.output(19,GPIO.LOW)
		if moisture>=73:

                        GPIO.setmode(GPIO.BCM)
                        GPIO.setwarnings(False)
                        GPIO.setup(21,GPIO.OUT)
                        GPIO.output(21,GPIO.HIGH)
                else:
                        GPIO.setup(21,GPIO.OUT)
                        GPIO.output(21,GPIO.LOW)
	

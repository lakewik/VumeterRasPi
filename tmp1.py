import alsaaudio as alsa
import time
import audioop
import math
import alsaaudio as aa
import audioop
from time import sleep
import smbus
import struct
import numpy as np
import wave
import time
import sys, os, time, atexit
from signal import SIGTERM
import subprocess
import urllib
from smbus import SMBus
from itertools import cycle
from time import sleep
from subprocess import call


alsa.cards()

# type 1 - standard GPIO
# type 2 - PCF8574 I2C Bus

vu_meter_type = 2


def SETGPIO(d):
	bus = SMBus(1)
	tak = 0
	bin_str_2 = "1" + "1" + "1" + "1" + "1" + "1" + "1" + "1"
	if (d == 'a'):
		bin_str_1 = "1" + "1" + "1" + "1" + "1" + "1" + "1" + "1"

	elif (d == 'b'):

		bin_str_1 = "0" + "1" + "1" + "1" + "1" + "1" + "1" + "1"
	elif (d == 'c'):
		bin_str_1 = "0" + "0" + "1" + "1" + "1" + "1" + "1" + "1"
	elif (d == 'd'):
		bin_str_1 = "0" + "0" + "0" + "1" + "1" + "1" + "1" + "1"
	elif (d == 'e'):
		bin_str_1 = "0" + "0" + "0" + "0" + "1" + "1" + "1" + "1"
	elif (d == 'f'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "1" + "1" + "1"
	elif (d == 'g'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "1" + "1"
	elif (d == 'h'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "1"
	elif (d == 'i'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
	elif (d == 'j'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "1" + "1" + "1" + "1" + "1" + "1" + "1"
	elif (d == 'k'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "0" + "1" + "1" + "1" + "1" + "1" + "1"
	elif (d == 'l'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "0" + "0" + "1" + "1" + "1" + "1" + "1"
	elif (d == 'm'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "0" + "0" + "0" + "1" + "1" + "1" + "1"
	elif (d == 'n'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "0" + "0" + "0" + "0" + "1" + "1" + "1"
	elif (d == 'o'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "0" + "0" + "0" + "0" + "0" + "1" + "1"
	elif (d == 'p'):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "1"
	elif (1 == 1):
		bin_str_1 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"
		bin_str_2 = "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0"







	hexa = int(hex(int(bin_str_1, 2)), 16)
	hexa2 = int(hex(int(bin_str_2, 2)), 16)
	bus.write_byte(0x23, hexa)
	bus.write_byte(0x21, hexa2)
	return



print "##############################"
print "# Waiting for a song to play #"
print "##############################"


#inp = alsa.PCM(type=alsa.PCM_CAPTURE,mode=alsa.PCM_NORMAL,card="plug:mixin")

#inp = alsa.PCM(alsa.PCM_CAPTURE, alsa.PCM_NORMAL, 'hw:Loopback,1,0')
out = alsa.PCM(alsa.PCM_PLAYBACK, alsa.PCM_NORMAL, 'plughw:0,0')

wavfile = wave.open('/root/download?file=i8e4i8f5g6h7a0g6','r')
sample_rate = wavfile.getframerate()
no_channels = wavfile.getnchannels()
chunk = 1024

#inp.setchannels(2)
#inp.setrate(44100)
#inp.setformat(alsa.PCM_FORMAT_S16_LE)
#inp.setperiodsize(220)

out.setchannels(2)
out.setrate(44100)
out.setformat(alsa.PCM_FORMAT_S16_LE)
out.setperiodsize(320)



status = 1

lo = 10000
hi = 32000

log_lo = math.log(lo)
log_hi = math.log(hi)
#data = wavfile.readframes(chunk)
#l = wavfile.readframes(chunk)
#while True:

#	if l:
#		try:
#			d = audioop.max(data, 2)
#			vu = (math.log(float(max(audioop.max(data, 2),1)))-log_lo)/(log_hi-log_lo)
#			teste = chr(ord('a')+min(max(int(vu*20),0),19))
#			if teste != 'a':
#				print teste
#			if d>0:
#				SETGPIO(teste)
#				if status:
#					print "Song found now playing!"
#					status = 0
#		except():
#			#GPIO.cleanup()
#			print "GPIO CLEAN"
#			print "Program Closed"

#			break
#out.write(data)
status = 1
while True:
    data = wavfile.readframes(chunk)
    out.write(data)
    d = audioop.max(data, 2)
    vu = (math.log(float(max(audioop.max(data, 2),1)))-log_lo)/(log_hi-log_lo)
    teste = chr(ord('a')+min(max(int(vu*20),0),19))
    print d
    if teste != 'a':
        print teste

    if d>0:
        SETGPIO(teste)
        if status:
            print "Song found now playing!"
            status = 0

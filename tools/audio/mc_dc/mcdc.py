import os
import sys
import math
import struct
import pyaudio
from datetime import datetime

# Variables
thresh = 0.002
sp = 0.01
RATE = 44100
spc = int(RATE * sp)
short_norm = (1.0 / 32768.0)
CHS = 2
fmt = pyaudio.paInt16
# -> Colors
gs = "\033[32m"
rs = "\033[31m"
ys = "\033[33m"
blue = "\033[34m"
ce = "\033[0m"
# -> Patterns
plus = gs + "[+] " + ce
minus = rs + "[-] " + ce
astk = blue + "[*] " + ce

class McDecoder:

	def mps(self, sample):
		count = len(sample) / 2
		format = "%dh" % (count)
		shorts = struct.unpack(format, sample)

		squares = 0.0
		for i in shorts:
			a = i * short_norm
			squares += a * a

		return math.sqrt(squares / count)

	def main(self):
		b = pyaudio.PyAudio()

		stream = b.open(format = fmt, channels = CHS, rate = RATE, input=True, frames_per_buffer = spc)

		thresh_final = thresh
		list_a = ""
		counter = 0

		for i in range(1000):
			try:
				sample = stream.read(spc)
				pass
			except IOError as e:
				print "\n" + rs + "[X] " + ce + gs + "Could not read recording, error -> " + str(e) + ce + "\n"
				pass

			amp = self.mps(sample)

			if amp > thresh:
				list_a += "1"
				pass
			else:
				list_a += "0"
				pass

		list_a = list_a.split("0")
		print gs + ">> " + ce + ys,list_a,ce
		for i in range(len(list_a)):
			if len(list_a[i]) == 45:
				print gs + " - " + ce
				pass
			elif len(list_a[i]) == 15:
				print gs + " . " + ce
				pass

def main():
	mcdc = McDecoder()

	mcdc.main()

if __name__ == '__main__':
	main()

#!/usr/bin/env python
#
#  newyear.py
#
#  Copyright (c) 2017-2020 Dominic Davis-Foster
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

# stdlib
import datetime
import sys
import time
import wave

# 3rd party
import pyaudio

# start time
target_time = datetime.datetime(2021, 1, 1, 0, 0, 0)
filename = "./02-09- In The Air Tonight.wav"

offset = datetime.timedelta(seconds=41, minutes=3)
start_time = target_time - offset
print(start_time)

# current time
print(time.time())

# from https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python
# length of data to read.
chunk = 1024

# open the file for reading.
wf = wave.open(filename, 'rb')

# create an audio object
p = pyaudio.PyAudio()

# open stream based on the wave object which has been input.
stream = p.open(
		format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True,
		)


def play():
	# read data (based on the chunk size)
	data = wf.readframes(chunk)

	# play stream (looping from beginning of file to the end)
	while data != '':
		# writing to the stream is what *actually* plays the sound.
		stream.write(data)
		data = wf.readframes(chunk)

	# cleanup stuff.
	stream.close()
	p.terminate()


# from http://quickies.seriot.ch/?id=397
while time.time() < time.mktime(start_time.timetuple()):
	print(f"{time.time()}\r", end='')
	sys.stdout.flush()

time.sleep(1.4)
play()

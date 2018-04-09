#!/usr/bin/python

import threading, os, time

wrt = threading.Semaphore()
mutex = threading.Semaphore()
readcount = 0

def write(idx, delay, counter):
	for i in range(counter):
		time.sleep(delay)
		print("Process {} is writing...".format(idx))

def read(idx, delay, counter):
	for i in range(counter):
		time.sleep(delay)
		print("Process {} is reading...".format(idx))

def activity():
	idx = int(threading.current_thread().name)
	global readcount
	if idx % 2:
		while True:
			# read
			mutex.acquire()
			readcount += 1
			if readcount == 1:
				wrt.acquire()
			mutex.release()
			read(idx, 1, 5)
			mutex.acquire()
			readcount -= 1
			if readcount == 0:
				wrt.release()
			mutex.release()
			break
	else:
		while True:
			# write
			wrt.acquire()
			write(idx, 1, 5)
			wrt.release()
			break

[threading.Thread(target = activity, name = str(i)).start() for i in range(6)]
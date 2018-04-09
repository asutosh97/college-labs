#!/usr/bin/python

import threading, os, time
from queue import Queue

MAX = 5
_buffer = Queue()
count = 0
full = threading.Semaphore(value = 0)
empty = threading.Semaphore(value = MAX)
mutex = threading.Semaphore(value = 1)

def produce():
	global count
	time.sleep(1)
	count += 1
	return count

def consume(item):
	time.sleep(1)
	print("{} item consumed...".format(item))

def activity():
	global _buffer
	idx = int(threading.current_thread().name)
	if idx:
		for i in range(20):
			# producer
			item = produce()
			print("{} item produced...".format(item))
			empty.acquire()
			mutex.acquire()
			_buffer.put(item)
			mutex.release()
			full.release()

	else:
		for i in range(20):
			# consumer
			full.acquire()
			mutex.acquire()
			item = _buffer.get()
			mutex.release()
			empty.release()
			consume(item)

[threading.Thread(target = activity, name = str(i)).start() for i in range(2)]

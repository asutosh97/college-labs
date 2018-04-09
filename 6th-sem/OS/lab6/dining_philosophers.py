#!/usr/bin/python

import threading, os, time

n = int(input("Enter the number of philosophers :- "))
chopstick = [threading.Semaphore() for _ in range(n)]

def eat(idx, delay, counter):
	for i in range(counter):
		time.sleep(delay)
		print("Process {} is eating...".format(idx))

def activity():
	idx = int(threading.current_thread().name)
	if idx == n-1:
		while True:
			chopstick[(idx + 1) % n].acquire()
			print("{} acquired {}".format(idx, (idx+1) % n))
			time.sleep(1)
			chopstick[idx].acquire()
			print("{} acquired {}".format(idx, idx))
			eat(idx, 1, 5)
			chopstick[idx].release()
			chopstick[(idx + 1) % n].release()
			break
	else:
		while True:
			chopstick[idx].acquire()
			print("{} acquired {}".format(idx, idx))
			time.sleep(1)
			chopstick[(idx + 1) % n].acquire()
			print("{} acquired {}".format(idx, (idx+1) % n))
			eat(idx, 1, 5)
			chopstick[(idx + 1) % n].release()
			chopstick[idx].release()
			break

[threading.Thread(target = activity, name = str(i)).start() for i in range(n)]

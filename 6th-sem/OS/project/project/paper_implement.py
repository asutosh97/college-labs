#!/usr/bin/python3
import sys, operator
from short_term_scheduler import *

def MLFQ(processes):
	processes_set1 = [process for process in processes if process['burst_time'] <= 10]
	remainder_processes = [process for process in processes if process not in processes_set1]
	remainder_processes = sorted(remainder_processes, key=lambda process: process['burst_time'])
	processes_set2 = remainder_processes[:int((3/4)*len(remainder_processes))]
	processes_set3 = [process for process in remainder_processes if process not in processes_set2]

	timer = 0
	result1, timer = rr(processes_set1, timer)
	result2, timer = sjf(processes_set2, timer)
	result3, timer = sjf(processes_set3, timer)

	return (result1 + result2 + result3)

def main():
	processes = []
	for _ in range(int(input("Enter number of processes :- "))):
		print("")
		process = {}
		process['id'] = _
		process['arrival_time'] = int(input("Enter arrival time of p%d:- " % _))
		process['burst_time'] = int(input("Enter burst time of p%d:- " % _))
		process['priority_value'] = int(input("Enter priority value of p%d:- " % _))
		process['time_left'] = process['burst_time']
		process['waiting_time'] = 0
		process['turn_around_time'] = 0
		process['rr_priority'] = 0
		processes.append(process)

	result = MLFQ(processes)
	result = sorted(result, key=lambda process: process['id'])
	print("PID\tPV\tAT\tBT\tWT\tTAT")
	for process in result:
		print("%d\t%d\t%d\t%d\t%d\t%d\t" % (process['id'], process['priority_value'], process['arrival_time'], process['burst_time'], process['waiting_time'], process['turn_around_time']))

if __name__ == "__main__":
	main()
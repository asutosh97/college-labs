#!/usr/bin/python3
import sys, operator
from short_term_scheduler import *

def MLFQ(processes):
	# separating processes that will go in each level
	time_quantum = 10
	processes_set1 = [process for process in processes if process['burst_time'] <= 10]
	remainder_processes = [process for process in processes if process not in processes_set1]
	remainder_processes = sorted(remainder_processes, key=lambda process: process['burst_time'])
	processes_set2 = remainder_processes[:int((3/4)*len(remainder_processes))]
	processes_set3 = [process for process in remainder_processes if process not in processes_set2]

	timer = 0
	gantt_chart = []
	
	# setting-up queue for level-one RR
	result1 = []
	ready_queue1 = PriorityQueue()
	processes_set1 = sorted(processes_set1, key=lambda process: process['arrival_time'])
	priority_counter1 = set_queue(ready_queue1, "rr_priority", processes_set1, 0, timer, 0)

	# setting-up queue for level-two SJF
	result2 = []
	ready_queue2 = PriorityQueue()
	processes_set2 = sorted(processes_set2, key=lambda process: process['arrival_time'])
	priority_counter2 = set_queue(ready_queue2, "burst_time", processes_set2, 0, timer, 0)

	# setting-up queue for level-three SJF
	result3 = []
	ready_queue3 = PriorityQueue()
	processes_set3 = sorted(processes_set3, key=lambda process: process['arrival_time'])
	priority_counter3 = set_queue(ready_queue3, "burst_time", processes_set3, 0, timer, 0)

	processes_left = len(processes)
	
	while processes_left:
		if not ready_queue1.empty():
			priority_counter1, timer_new, processes_left, gantt_chart = rr_step(processes_set1, ready_queue1, result1, timer, processes_left, gantt_chart, time_quantum, priority_counter1)
			priority_counter2 = set_queue(ready_queue2, "burst_time", processes_set2, timer + 1, timer_new, priority_counter2)
			priority_counter3 = set_queue(ready_queue3, "burst_time", processes_set3, timer + 1, timer_new, priority_counter3)
			timer = timer_new
		elif not ready_queue2.empty():
			priority_counter2, timer_new, processes_left, gantt_chart = sjf_step(processes_set2, ready_queue2, result2, timer, processes_left, gantt_chart, time_quantum, priority_counter1)
			priority_counter1 = set_queue(ready_queue1, "rr_priority", processes_set1, timer + 1, timer_new, priority_counter1)
			priority_counter3 = set_queue(ready_queue3, "burst_time", processes_set3, timer + 1, timer_new, priority_counter3)
			timer = timer_new
		elif not ready_queue3.empty():
			priority_counter3, timer_new, processes_left, gantt_chart = sjf_step(processes_set3, ready_queue3, result3, timer, processes_left, gantt_chart, time_quantum, priority_counter1)
			priority_counter1 = set_queue(ready_queue1, "rr_priority", processes_set1, timer + 1, timer_new, priority_counter1)
			priority_counter2 = set_queue(ready_queue2, "burst_time", processes_set2, timer + 1, timer_new, priority_counter2)
			timer = timer_new
		else:
			timer += 1
			priority_counter1 = set_queue(ready_queue1, "rr_priority", processes_set1, timer, timer, priority_counter1)
			priority_counter2 = set_queue(ready_queue2, "burst_time", processes_set2, timer, timer, priority_counter2)
			priority_counter3 = set_queue(ready_queue3, "burst_time", processes_set3, timer, timer, priority_counter3)

	return (result1 + result2 + result3), gantt_chart

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

	result, gantt_chart = MLFQ(processes)
	result = sorted(result, key=lambda process: process['id'])
	print("PID\tPV\tAT\tBT\tWT\tTAT")
	for process in result:
		print("%d\t%d\t%d\t%d\t%d\t%d\t" % (process['id'], process['priority_value'], process['arrival_time'], process['burst_time'], process['waiting_time'], process['turn_around_time']))
	print("")
	for process in gantt_chart:
		print(process)

if __name__ == "__main__":
	main()
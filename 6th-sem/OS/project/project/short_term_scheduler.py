#!/usr/bin/python3
'''
Program to simulate different scheduling alogrithms
'''
from queue import PriorityQueue

def insert_to_ready_queue(ready_queue, criteria, process, priority_counter):
	priority_counter += 1
	process['rr_priority'] = priority_counter
	ready_queue.put((process[criteria], process))
	return priority_counter

def set_queue(ready_queue, criteria, processes, current_time, priority_counter):
	for process in processes:
		if process['arrival_time'] == current_time:
			priority_counter = insert_to_ready_queue(ready_queue, criteria, process, priority_counter)
	return priority_counter

def initialize_queue(ready_queue, criteria, processes, current_time, priority_counter):
	for process in processes:
		if process['arrival_time'] <= current_time:
			priority_counter = insert_to_ready_queue(ready_queue, criteria, process, priority_counter)
	return priority_counter

def base_scheduler(processes, time_quantum, is_preemptive, criteria, time0):
	result = []
	priority_counter = 0
	timer = time0
	ready_queue = PriorityQueue()

	priority_counter = initialize_queue(ready_queue, criteria, processes, timer, priority_counter)
	processes_left = len(processes)

	while processes_left:
		if not ready_queue.empty():
			_, process = ready_queue.get()
			runtime = min(time_quantum, process['time_left']) if is_preemptive else process['time_left']
			process['time_left'] -= runtime
			old_timer = timer
			timer += runtime

			for time in range(old_timer + 1, timer + 1):
				priority_counter = set_queue(ready_queue, criteria, processes, time, priority_counter)

			if process['time_left'] == 0:
				process['turn_around_time'] = timer - process['arrival_time']
				process['waiting_time'] = process['turn_around_time'] - process['burst_time']
				processes_left -= 1
				result.append(process)
			else:
				priority_counter = insert_to_ready_queue(ready_queue, criteria, process, priority_counter)
		else:
			timer += 1
			priority_counter = set_queue(ready_queue, criteria, processes, timer, priority_counter)
			
	return result, timer

def fcfs(processes, time0):
	return base_scheduler(processes, 1, False, 'arrival_time', time0)

def sjf(processes, time0):
	return base_scheduler(processes, 1, False, 'burst_time', time0)

def srtf(processes, time0):
	return base_scheduler(processes, 1, True, 'time_left', time0)

def rr(processes, time0):
	return base_scheduler(processes, int(input('Enter time quantum : ')), True, 'rr_priority', time0)

def priority_non_preemptive(processes, time0):
	return base_scheduler(processes, 1, False, 'priority_value', time0)

def priority_preemptive(processes, time0):
	return base_scheduler(processes, 1, True, 'priority_value', time0)

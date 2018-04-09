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

def base_scheduler(processes, time_quantum, is_preemptive, criteria):
	result = []
	priority_counter = 0
	timer = 0
	ready_queue = PriorityQueue()

	priority_counter = set_queue(ready_queue, criteria, processes, timer, priority_counter)
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
			
	return result

def fcfs(processes):
	return base_scheduler(processes, 1, False, 'arrival_time')

def sjf(processes):
	return base_scheduler(processes, 1, False, 'burst_time')

def srtf(processes):
	return base_scheduler(processes, 1, True, 'time_left')

def rr(processes):
	return base_scheduler(processes, int(input('Enter time quantum : ')), True, 'rr_priority')

def priority_non_preemptive(processes):
	return base_scheduler(processes, 1, False, 'priority_value')

def priority_preemptive(processes):
	return base_scheduler(processes, 1, True, 'priority_value')

def switcher(scheduling_algo, processes):
	return {
		'1': fcfs,
		'2': sjf,
		'3': srtf,
		'4': rr,
		'5': priority_non_preemptive,
		'6': priority_preemptive
	}[scheduling_algo](processes)

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

	print("Select your scheduling algorithm")
	print("1. FCFS")
	print("2. SJF")
	print("3. SRTF")
	print("4. RR")
	print("5. Priority non-preemptive")
	print("6. Priority preemptive")

	result = switcher(input(), processes)
	result = sorted(result, key=lambda process: process['id'])
	print("PID\tAT\tBT\tPV\tTAT\tWT")
	for process in result:
		print("%d\t%d\t%d\t%d\t%d\t%d\t" % (process['id'], process['arrival_time'], process['burst_time'], process['priority_value'], process['turn_around_time'], process['waiting_time']))

if __name__ == "__main__":
	main()

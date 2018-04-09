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

def set_queue(ready_queue, criteria, processes, start_time, end_time, priority_counter):
	# assumes the processes are sorted in the list "processes" in ascending order of arrival time.
	# note :- sorting must be stable so that 2 processes with same arrival time then process id lower should be 1st
	given_range = range(start_time, end_time + 1)
	for process in processes:
		if process['arrival_time'] in given_range:
			priority_counter = insert_to_ready_queue(ready_queue, criteria, process, priority_counter)
	return priority_counter

def base_scheduler_step(processes, ready_queue, result, timer, time_quantum, is_preemptive, criteria, priority_counter, processes_left, gantt_chart):
	_, process = ready_queue.get()
	runtime = min(time_quantum, process['time_left']) if is_preemptive else process['time_left']
	process['time_left'] -= runtime
	old_timer = timer
	timer += runtime

	priority_counter = set_queue(ready_queue, criteria, processes, old_timer + 1,  timer, priority_counter)
	gantt_chart.append({'id': process['id'], 'start_time': old_timer, 'end_time': timer})

	if process['time_left'] == 0:
		process['turn_around_time'] = timer - process['arrival_time']
		process['waiting_time'] = process['turn_around_time'] - process['burst_time']
		processes_left -= 1
		result.append(process)
	else:
		priority_counter = insert_to_ready_queue(ready_queue, criteria, process, priority_counter)

	return priority_counter, timer, processes_left, gantt_chart

def fcfs_step(processes, ready_queue, result, timer, processes_left, gantt_chart, time_quantum, priority_counter):
	return base_scheduler_step(processes, ready_queue, result, timer, 1, False, 'arrival_time', 0, processes_left, gantt_chart)

def sjf_step(processes, ready_queue, result, timer, processes_left, gantt_chart, time_quantum, priority_counter):
	return base_scheduler_step(processes, ready_queue, result, timer, 1, False, 'burst_time', 0, processes_left, gantt_chart)

def srtf_step(processes, ready_queue, result, timer, processes_left, gantt_chart, time_quantum, priority_counter):
	return base_scheduler_step(processes, ready_queue, result, timer, 1, True, 'time_left', 0, processes_left, gantt_chart)

def rr_step(processes, ready_queue, result, timer, processes_left, gantt_chart, time_quantum, priority_counter):
	return base_scheduler_step(processes, ready_queue, result, timer, time_quantum, True, 'rr_priority', priority_counter, processes_left, gantt_chart)

def priority_non_preemptive_step(processes, ready_queue, result, timer, processes_left, gantt_chart, time_quantum, priority_counter):
	return base_scheduler_step(processes, ready_queue, result, timer, 1, False, 'priority_value', 0, processes_left, gantt_chart)

def priority_preemptive_step(processes, ready_queue, result, timer, processes_left, gantt_chart, time_quantum, priority_counter):
	return base_scheduler_step(processes, ready_queue, result, timer, 1, True, 'priority_value', 0, processes_left, gantt_chart)

def base_scheduler(processes, time_quantum, is_preemptive, criteria, time0):
	result = []
	priority_counter = 0
	timer = time0
	gantt_chart = []
	ready_queue = PriorityQueue()
	processes = sorted(processes, key=lambda process: process['arrival_time'])

	priority_counter = set_queue(ready_queue, criteria, processes, 0, timer, priority_counter)
	processes_left = len(processes)

	while processes_left:
		if not ready_queue.empty():
			priority_counter, timer, processes_left, gantt_chart = base_scheduler_step(processes, ready_queue, result, timer, time_quantum, 
																	is_preemptive, criteria, priority_counter, processes_left, gantt_chart)
		else:
			timer += 1
			priority_counter = set_queue(ready_queue, criteria, processes, timer, timer, priority_counter)
			
	return result, gantt_chart, timer

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

def switcher(scheduling_algo, processes):
	return {
		'1': fcfs,
		'2': sjf,
		'3': srtf,
		'4': rr,
		'5': priority_non_preemptive,
		'6': priority_preemptive
	}[scheduling_algo](processes, 0)

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

	result, gantt_chart, _ = switcher(input(), processes)
	result = sorted(result, key=lambda process: process['id'])
	print("PID\tAT\tBT\tPV\tTAT\tWT")
	for process in result:
		print("%d\t%d\t%d\t%d\t%d\t%d\t" % (process['id'], process['arrival_time'], process['burst_time'], process['priority_value'], process['turn_around_time'], process['waiting_time']))
	print("")
	for process in gantt_chart:
		print(process)

if __name__ == "__main__":
	main()

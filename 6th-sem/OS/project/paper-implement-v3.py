#!/usr/bin/python3
import sys, operator
from short_term_scheduler import *
from functools import reduce

def MLFQ(processes):
	# According to our research paper
	n_queues = 3
	
	def condition_one_base(op):
		def condition_one(process):
			return op(process['burst_time'], 10)
		return condition_one

	q23 = sorted(filter(condition_one_base(operator.gt), processes), key=lambda process: process['burst_time'])
	threshold_bt = q23[:int((3/4)*len(q23))][-1]["burst_time"]

	def condition_two(process):
		return (process['burst_time'] <= threshold_bt)

	def condition_three(process):
		return (process['burst_time'] > threshold_bt)

	queue_details = [{'step_function': rr_step, 'criteria': 'rr_priority', 'condition': condition_one_base(operator.le), 'time_quantum': 10},
					{'step_function': sjf_step, 'criteria': 'burst_time', 'condition': condition_two, 'time_quantum': 10},
					{'step_function': sjf_step, 'criteria': 'burst_time', 'condition': condition_three, 'time_quantum': 10}]

	return MLFQ_base(n_queues, queue_details, processes)

def MLFQ_base(n_queues, queue_details, processes):
	# set processes of each level in the MLFQ
	processes_copy = processes[:]
	processes_set = []
	for i in range(n_queues - 1):
		processes_set.append(list(filter(queue_details[i]["condition"], processes_copy)))
		processes_copy = [process for process in processes_copy if process not in processes_set[i]]
	processes_set.append(processes_copy)

	for p_set in processes_set:
		for process in p_set:
			print(process)
		print(" ")

	result = [[] for _ in range(n_queues)]
	ready_queue = [PriorityQueue() for _ in range(n_queues)]
	timer = 0
	gantt_chart = []
	priority_counter = [[0] for _ in range(n_queues)]

	# setting up queues
	for idx in range(n_queues):
		processes_set[idx].sort(key = lambda process: process['arrival_time'])
		priority_counter[idx] = set_queue(ready_queue[idx], queue_details[idx]["criteria"], processes_set[idx], 0, timer, 0)

	processes_left = len(processes)
	
	while processes_left:
		entered_for = False
		for idx in range(n_queues):
			if not ready_queue[idx].empty():
				entered_for = True
				priority_counter[idx], timer_new, processes_left, gantt_chart = queue_details[idx]['step_function'](processes_set[idx], ready_queue[idx], result[idx], timer, processes_left, gantt_chart, queue_details[idx]['time_quantum'], priority_counter[idx])
				for step_idx in range(1, n_queues):
					next_idx = (idx + step_idx) % n_queues
					priority_counter[next_idx] = set_queue(ready_queue[next_idx], queue_details[next_idx]["criteria"], processes_set[next_idx], timer + 1, timer_new, priority_counter[next_idx])
				timer = timer_new
				break

		if not entered_for:
			timer += 1
			for idx in range(n_queues):
				priority_counter[idx] = set_queue(ready_queue[idx], queue_details[idx]['criteria'], processes_set[idx], timer, timer, priority_counter[idx])

	def concat(a, b):
		return a + b

	return reduce(concat, result), gantt_chart

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

'''
Future thoughts :-
1. make a base MLQ function which takes argument the number of levels, and the conditions to set each level
'''
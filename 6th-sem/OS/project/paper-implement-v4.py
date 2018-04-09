#!/usr/bin/python3
import sys, operator
from short_term_scheduler3 import *
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

	queue_details = [{'scheduling_algo': 'rr', 'condition': condition_one_base(operator.le), 'time_quantum': 10},
					{'scheduling_algo': 'sjf', 'condition': condition_two, 'time_quantum': 10},
					{'scheduling_algo': 'sjf', 'condition': condition_three, 'time_quantum': 10}]

	return MLFQ_base(n_queues, queue_details, processes, 0)


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

	result, gantt_chart, _ = MLFQ(processes)
	result = sorted(result, key=lambda process: process['id'])
	print("PID\tPV\tAT\tBT\tWT\tTAT")
	for process in result:
		print("%d\t%d\t%d\t%d\t%d\t%d\t" % (process['id'], process['priority_value'], process['arrival_time'], process['burst_time'], process['waiting_time'], process['turn_around_time']))
	print("")
	for process in gantt_chart:
		print(process)

if __name__ == "__main__":
	main()

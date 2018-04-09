#!/usr/bin/python3
import sys, operator

def safe(allocation, maximum, available):
	n = len(allocation)
	m = len(allocation[0])
	need = [list(map(operator.sub, maximum[i], allocation[i])) for i in range(n)]

	work = available[:]
	finish = [False for _ in range(n)]

	while True:
		entered_if = False
		for i in range(n):
			if (not finish[i]) and all([need[i][j] <= work[j] for j in range(m)]):
				entered_if = True
				work = list(map(operator.add, work, allocation[i]))
				finish[i] = True
				break
		
		if not entered_if:
			break

	return all(finish)

def base_alloc_dealloc(available, request, allocation, idx, op1, op2):
	available = list(map(op1, available, request))
	allocation[idx] = list(map(op2, allocation[idx], request))
	return available, allocation


def pretend_allocation(available, request, allocation, idx):
	return base_alloc_dealloc(available, request, allocation, idx, operator.sub, operator.add)

def reverse_pretended_allocation(available, request, allocation, idx):
	return base_alloc_dealloc(available, request, allocation, idx, operator.add, operator.sub)


def process_request(allocation, maximum, available, idx, request):
	n = len(allocation)
	m = len(allocation[0])
	need = [list(map(operator.sub, maximum[i], allocation[i])) for i in range(n)]

	if not all([request[i] <= need[idx][i] for i in range(m)]):
		print("Process exceeded maximum claim")
		return False

	if not all([request[i] <= available[i] for i in range(m)]):
		print("Enough resouces currently not available")
		return False

	available, allocation = pretend_allocation(available, request, allocation, idx)
	status = safe(allocation, maximum, available)
	available, allocation = reverse_pretended_allocation(available, request, allocation, idx)

	return status

def main():
	n = int(input("Enter number of processes(n) :- "))
	m = int(input("Enter number of resources(m) :- "))

	print("Enter the allocation matrix (n x m) :- ")
	allocation = [[int(x) for x in input().split()] for _ in range(n)]

	print("Enter the maximum matrix (n x m) :- ")
	maximum = [[int(x) for x in input().split()] for _ in range(n)]
	
	print("Enter the available list (n) :- ")
	available = [int(x) for x in input().split()]

	if not safe(allocation, maximum, available):
		print("Initial configuration isn't safe")
		sys.exit()

	while True:
		idx = int(input("Enter the process which needs to request resources (0 indexed) :- "))
		print("Enter the resource request list (n) :- ")
		request = [int(x) for x in input().split()]
		if process_request(allocation, maximum, available, idx, request):
			print("Request granted")
		else:
			print("Not granted")

if __name__ == "__main__":
	main()
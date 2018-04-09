import threading, sys

results = []

def multiply(thread_arg):
	global results
	row_index = thread_arg['row_index']
	col_index = thread_arg['col_index']

	row = thread_arg['row']
	col = thread_arg['col']

	for i in range(len(row)):
		results[row_index][col_index] += row[i] * col[i]

if __name__ == "__main__":
	r1, c1 = [int(x) for x in input("Enter the dimensions of the 1st matrix :- ").split()]
	r2, c2 = [int(x) for x in input("Enter the dimensions of the 1st matrix :- ").split()]

	if not c1 == r2:
		print("matrices are not compatible")
		sys.exit()

	results = [[0] * c2 for i in range(r1)]
	print("Enter the values of the 1st matrix :- ")
	m1 = [[int(x) for x in input().split()] for i in range(r1)]
	print("Enter the values of the 2nd matrix :- ")
	m2 = [[int(x) for x in input().split()] for i in range(r2)]
	m2_t = list(zip(*m2))

	n_threads = r1 * c2

	threads = []
	for i in range(r1):
		for j in range(c2):
			thread_arg = {'row_index': i, 'col_index': j, 'row': m1[i], 'col': m2_t[j]}
			threads.append(threading.Thread(target = multiply, args=(thread_arg,)))
			threads[-1].start()


	for i in range(n_threads):
		threads[i].join()

	for result in results:
		print(result)

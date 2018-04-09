import threading

total_sum = 0

def calc_sum(thread_arg):
	global total_sum
	for i in range(thread_arg['beg'], thread_arg['end'] + 1):
		total_sum += i

if __name__ == "__main__":
	n = int(input("Enter the amount to be summed to :- "))
	n_threads = int(input("Enter the no. of threads :- "))

	width = int(n / n_threads)
	
	threads = []
	for i in range(n_threads):
		thread_arg = {'beg': i * width + 1, 'end': (i + 1) * width}
		threads.append(threading.Thread(target = calc_sum, args=(thread_arg,)))
		threads[i].start()

	for i in range(n_threads):
		threads[i].join()

	print("sum = {}".format(total_sum))
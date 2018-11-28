from multiprocessing import Queue, Process

def consumer(input_q):
	while True:
		item = input_q.get()
		if item is None:
			break
		print(item)
	print("Consumer done")

def producer(sequence, output_q):
	for item in sequence:
		output_q.put(item)

if __name__ == '__main__':
	q = Queue()

	cons_p = Process(target=consumer, args=(q,))
	cons_p.start()

	sequence = [1,2,3,4]
	producer(sequence, q)

	q.put(None)

	cons_p.join()

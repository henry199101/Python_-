from multiprocessing import Process, Queue

def consumer(q):
	while True:
		item = q.get()

		if item is None:
			break

		print(item)


def producer(sequence, q):
	for item in sequence:
		q.put(item)


if __name__ == "__main__":
	q = Queue()

	consumer_process = Process(target=consumer, args=(q,))
	
	consumer_process.start()

	sequence = [1, 2, 3, 4]
	producer(sequence, q)

	q.put(None)

	consumer_process.join()

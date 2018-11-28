from multiprocessing import Process, JoinableQueue

def consumer(q):
	while True:
		item = q.get()

		print(item)

		q.task_done()


def producer(sequence, q):
	for item in sequence:
		q.put(item)


if __name__ == "__main__":
	q = JoinableQueue()
	consumer_process = Process(target=consumer, args=(q,))
	consumer_process.daemon = True
	consumer_process.start()

	sequence = [1, 2, 3, 4]
	producer(sequence, q)

	q.join()

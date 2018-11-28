from multiprocessing import JoinableQueue, Process

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
	consumer_process1 = Process(target=consumer, args=(q,))
	consumer_process2 = Process(target=consumer, args=(q,))

	consumer_process1.daemon = True
	consumer_process2.daemon = True

	consumer_process1.start()
	consumer_process2.start()

	sequence = list(range(1, 101))
	producer(sequence, q)

	q.join()

from multiprocessing import Process, JoinableQueue

def consumer(q):
	while True:
		# 从队列 q 中获取项 item
		item = q.get()
		
		# 处理 item
		print(item)

		q.task_done()
	

def producer(sequence, q):
	for item in sequence:
		q.put(item)


if __name__ == "__main__":
	q = JoinableQueue()
	consumer_process = Process(target=consumer, args=(q,))

	# 将进程 consumer_process 设置为 后台进程；
	# 后台进程会随着主进程终止而终止。
	consumer_process.daemon = True
	
	# 启动消费者进程
	consumer_process.start()

	sequence = [1, 2, 3, 4]
	producer(sequence, q)

	# 主进程等待消费者进程处理完队列 q 中的所有项，
	# 然后主进程再往下执行。
	q.join()
	# q.join() 之后没有代码，主进程终止；
	# 进程 consumer_process 是后台进程，随之终止。

	"""
	q.join()
	"""

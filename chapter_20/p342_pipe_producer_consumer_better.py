from multiprocessing import Process, Pipe

def consumer(pipe):
	output_side, input_side = pipe

	input_side.close()

	while True:
		try:
			item = output_side.recv()
		except EOFError:
			break

		print(item)

	output_side.close()

	print("Consumer done!")


def producer(sequence, pipe):
	output_side, input_side = pipe

	output_side.close()

	for item in sequence:
		input_side.send(item)

	input_side.close()


if __name__ == "__main__":
	pipe = Pipe()

	consumer_process = Process(target=consumer, args=(pipe,))
	consumer_process.start()

	sequence = [1, 2, 3, 4]
	producer(sequence, pipe)

	consumer_process.join()

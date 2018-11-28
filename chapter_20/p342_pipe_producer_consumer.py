from multiprocessing import Pipe, Process

def consumer(pipe):
	output_p, input_p = pipe
	input_p.close()
	while True:
		try:
			item = output_p.recv()
		except EOFError:
			break
		print(item)
	print("Consumer done")

def producer(sequence, input_p):
	for item in sequence:
		input_p.send(item)

if __name__ == "__main__":
	(output_p, input_p) = Pipe()
	cons_p = Process(target=consumer, args=((output_p, input_p),))
	cons_p.start()

	output_p.close()

	sequence = [1,2,3,4]
	producer(sequence, input_p)

	input_p.close()

	cons_p.join()

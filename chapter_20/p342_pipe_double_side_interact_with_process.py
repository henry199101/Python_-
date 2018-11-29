from multiprocessing import Process, Pipe

def adder(pipe):
	server_side, client_side = pipe

	client_side.close()

	while True:
		try:
			x, y = server_side.recv()
		except EOFError:
			break

		result = x + y

		server_side.send(result)

	print("Done!")


if __name__ == '__main__':
	pipe = Pipe()

	server_side, client_side = pipe

	adder_process = Process(target=adder, args=(pipe,))
	adder_process.start()

	server_side.close()

	client_side.send((3, 4))
	print(client_side.recv())

	client_side.send(('Hello, ', 'World!'))
	print(client_side.recv())

	client_side.close()

	adder_process.join()

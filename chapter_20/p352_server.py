from multiprocessing.connection import Listener

server = Listener(address=('', 15000), authkey='12345')

while True:
	conn = server.accept()

	while True:
		try:
			x, y = conn.recv()
		except EOFError:
			break

		result = x + y

		conn.send(result)

	conn.close()

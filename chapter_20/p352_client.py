from multiprocessing.connection import Client

conn = Client(address=('localhost', 15000), authkey='12345')

conn.send((2, 3))
result = conn.recv()
print(result)

conn.send(('Hello, ', 'World!'))
result = conn.recv()
print(result)

conn.close()

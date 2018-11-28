from threading import Thread
from time import ctime, sleep

def clock(interval):
	while True:
		print("The time is %s" % ctime())
		sleep(interval)

t = Thread(target=clock, args=(2,))
#t.daemon = False
t.start()


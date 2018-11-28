from multiprocessing import Process
from time import ctime, sleep

class ClockProcess(Process):
	def __init__(self, interval):
		Process.__init__(self)
		self.interval = interval
	def run(self):
		while True:
			print("The time is %s" % ctime())
			sleep(self.interval)

if __name__ == "__main__":
	p = ClockProcess(2)
	p.start()

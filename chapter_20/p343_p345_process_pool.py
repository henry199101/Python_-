# 程序来自廖雪峰Python
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000#0

from multiprocessing import Pool
from time import time, sleep
from os import getpid
from random import random


def long_time_task(name):
	print("Task %s (%s) starts..." % (name, getpid()))
	start = time()
	sleep(random() * 3)
	end = time()
	elapsed_time = end - start
	print("Task %s runs %.2f seconds!" % (name, elapsed_time))


if __name__ == "__main__":
	print("Main process (%s) starts..." % getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print("Waiting for all subprocesses done!")
	p.close()
	p.join()
	print("All subprocesses done!")

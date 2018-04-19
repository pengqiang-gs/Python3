# _*_ coding: utf-8

import time, functools

def execute_time(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		begin = time.time()
		result = func(*args, **kw)
		end = time.time()
		print('function %s run costs %.5f seconds.' % (func.__name__, end - begin))
		return result
	return wrapper

@execute_time
def testing():
	for item in range(1, 1000000):
		pass

if __name__ == '__main__':
	testing()

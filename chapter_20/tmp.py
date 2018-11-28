def decorate(func):
	def inner(*args, **kwargs):
		print('function ' + func.__name__ + ' running...')
		return func(*args, **kwargs)
		
	return inner

@decorate
def f(x):
	print(x)
	return x

#f(1)i

@decorate
def g(*args, **kwargs):
	return sum(args) + sum(kwargs.values())

print(g(1, 2, a=3, b=4))

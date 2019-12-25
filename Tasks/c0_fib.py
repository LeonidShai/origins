def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	#print(n)
	if n < 0:
		raise ValueError
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	#print(n)
	a = 0
	b = 1
	if n < 0:
		raise ValueError
	elif n == 1:
		return a
	elif n == 2:
		return b
	else:
		i = 2
		chislo = 0
		while i <= n:
			chislo = a + b
			a, b = b, chislo
			i += 1
		return chislo

if __name__ == "__main__":
	print(fib_recursive(8))
	print(fib_iterative(9))
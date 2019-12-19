"""
Taylor series
"""
from typing import Union
import math

def ex(x: Union[int, float], delta=0.0001) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	print(x)
	if x == 0:
		return 1
	else:
		result_sum = 1
		n = 1
		while True:
			result = (x ** n) / math.factorial(n)
			if result < delta:
				return result_sum
			else:
				result_sum += result
				n += 1



def sinx(x: Union[int, float], delta=0.0001) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	result_sum = x
	print(x)
	return 0




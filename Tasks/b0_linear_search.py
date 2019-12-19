"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import numpy as np
import time

def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	print(arr)
	k = min(arr)
	for i in range(len(arr)):
		if arr[i] == k:
			return i
	return -1

def finding_elem(find_elem, array):
	index = None
	for i, elem in enumerate(array):
		if elem == find_elem:
			index = i
			return index
	return index

if __name__ == "__main__":
	n = 1000
	array = np.arange(n)
	find_elem = np.random.choice(array)
	print(find_elem)
	np.random.shuffle(array)
	print(finding_elem(find_elem, array))
	print(min_search([4, 1, 9, 1, 9, 3]))

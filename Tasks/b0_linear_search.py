"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	print(arr)
	n = min(arr)
	for i in range(len(arr)):
		if arr[i] == n:
			return i
	return -1

if __name__ == "__main__":
	print(min_search([4, 1, 9, 1, 9, 3]))

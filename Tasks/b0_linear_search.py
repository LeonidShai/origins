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
	min_index = None
	min_elem = arr[0]
	for i in range(1, len(arr)):
		if min_elem > arr[i]:
			min_elem = arr[i]
			min_index = i
	return min_index

if __name__ == "__main__":
	print(min_search([4, 1, 9, 1, 9, 3]))

from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	arr = list(arr)
	arr.sort()

	print(elem, arr)

	return None

if __name__ == "__main__":
	print(binary_search(3, [1, 6, 2, 3, 5, 9]))
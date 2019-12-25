from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	print(elem, arr)
	left = 0
	right = len(arr)
	middle = (right + left) // 2
	if elem == arr[middle]:
		return middle
	elif elem > arr[middle]:
		left = middle + 1
	else:
		right = middle - 1

	binary_search(elem, arr)



if __name__ == "__main__":
	print(binary_search(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

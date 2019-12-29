from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence, left = 0, right = None) -> Optional[int]:
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	if right is None:
		right = len(arr) - 1

	if elem < arr[0] or elem > arr[-1]:
		return None

	middle = (right + left) // 2
	if elem == arr[middle]:
		return middle
	elif elem > arr[middle]:
		if left == right:
			return None
		else:
			return binary_search(elem, arr, middle+1, right)
	else:
		if left == right:
			return None
		else:
			return binary_search(elem, arr, left, middle-1)



if __name__ == "__main__":
	arrr = [i for i in range(10)] + [11]
	print(arrr)
	print(binary_search(10, arrr))

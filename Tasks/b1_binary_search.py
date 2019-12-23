from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	right = len(arr)
	left = 0
	while True:
		middle = (right + left) // 2
		if elem == arr[middle]:
			return middle
		elif arr[middle] > elem:
			right = middle - 1
		else:
			left = middle + 1


if __name__ == "__main__":
<<<<<<< Updated upstream
	print(binary_search(3, [1, 6, 2, 3, 5, 9]))
=======
	array = [i for i in range(1, 11)]
	find_elem = 11 #random.choice(array)
	print(f"find_elem {find_elem}")
	print(array)
	print("index:", bn_search_elem(find_elem, array))
>>>>>>> Stashed changes

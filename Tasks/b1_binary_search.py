from typing import Any, Sequence, Optional
import random

def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	print(elem, arr)
	return None


def bn_search_elem(find_elem, array):
	right = len(array)
	left = 0
	middle = (right + left)//2
	while middle > -1:
		print(f"{array[middle]}")
		if find_elem == array[middle]:
			return middle
		else:
			if array[middle] > find_elem:
				right = middle
				left = 0
				middle = (right + left)//2
			else:
				right = len(array)
				left = middle
				middle = (right + left)//2


if __name__ == "__main__":
	array = [i for i in range(1, 11)]
	find_elem = 4 #random.choice(array)
	print(f"find_elem {find_elem}")
	print(array)
	print("index:", bn_search_elem(find_elem, array))
from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	N = len(container)
	for i in range(N - 1):
		for j in range(N - i - 1):
			if container[j] > container[j + 1]:
				container[j], container[j + 1] = container[j + 1], container[j]
	return container

if __name__ == "__main__":
	import random
	N = 10
	shuffle_list = list(range(N))
	random.shuffle(shuffle_list)
	print(shuffle_list)
	for i in range(N - 1):
		for j in range(N - i - 1):
			if shuffle_list[j] > shuffle_list[j + 1]:
				shuffle_list[j], shuffle_list[j + 1] = shuffle_list[j + 1], shuffle_list[j]

	print(shuffle_list)
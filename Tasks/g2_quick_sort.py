from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) < 2:
		return container
	else:
		oporn_elem = container[0]
		less = []
		greater = []
		for i in container[1:]:
			if i <= oporn_elem:
				less.append(i)
			else:
				greater.append(i)
		return sort(less) + [oporn_elem] + sort(greater)


if __name__ == "__main__":
	import random
	array = [random.randint(0, 9) for i in range(8)]
	print(array)
	print(sort(array))


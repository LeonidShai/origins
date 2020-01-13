from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) <= 1:
		return container
	else:
		middle = len(container) // 2
		left_container = sort(container[:middle])
		right_container = sort(container[middle:])

	return merge(left_container, right_container)

def merge(left_container, right_container):
	sorted_ = []
	left_container_index = 0
	right_container_index = 0
	left_container_length = len(left_container)
	right_container_length = len(right_container)

	for _ in range(left_container_length + right_container_length):
		if (left_container_index < left_container_length) and (right_container_index < right_container_length):
			if left_container[left_container_index] <= right_container[right_container_index]:
				sorted_.append(left_container[left_container_index])
				left_container_index += 1
			else:
				sorted_.append(right_container[right_container_index])
				right_container_index += 1

		elif left_container_index == left_container_length:
			sorted_.append(right_container[right_container_index])
			right_container_index += 1
		elif right_container_index == right_container_length:
			sorted_.append(left_container[left_container_index])
			left_container_index += 1

	return sorted_


if __name__ == "__main__":
	array = [6, 5, 1, 2, 10, 9, 1]
	print(sort(array))
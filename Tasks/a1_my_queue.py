"""
My little Queue
"""
from typing import Any

queue = []

def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	print(f"Add {elem} in the end")
	global queue
	queue.append(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if no elements.

	:return: dequeued element
	"""
	global queue
	if not queue:
		return None
	else:
		n = queue[0]
		del queue[0]
		return n


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	print(f"Index {ind} of element")
	global queue
	if ind >= len(queue):
		return None
	else:
		return queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	queue = []
	return None

if __name__ == "__main__":
	enqueue(3)
	enqueue(4)
	enqueue(1)
	print(queue)
	print("return first elem:", dequeue())
	print(queue)
	print(peek(0))
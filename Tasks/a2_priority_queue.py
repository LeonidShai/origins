"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

que_pr = dict()

def enqueue(elem: Any, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""

	global que_pr
	#print(f"Add {elem} with {priority} at the queue")
	if priority in que_pr:
		que_pr[priority].append(elem)
	else:
		que_pr[priority] = [elem]

	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if not elements.

	:return: dequeued element
	"""
	if not que_pr:
		return None
	else:
		prior_min = min([key for key in que_pr.keys()])
		k = que_pr[prior_min][0]
		del que_pr[prior_min][0]
		return k


def peek(ind: int = 0, priority: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global que_pr
	l = []
	for key in que_pr.keys():
		l.append(key)
	l.sort()

	a = []
	for i in l:
		for j in que_pr[i]:
			a.append(j)

	if ind >= len(a):
		return None
	else:
		return a[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global que_pr
	que_pr = {}
	return None

if __name__ == "__main__":
	enqueue(3, 1)
	enqueue(2, 0)
	enqueue(1, 2)
	enqueue(4, 0)
	print(que_pr)
	print(peek(2))
	print(dequeue())
	print(que_pr)
	clear()
	print(que_pr)
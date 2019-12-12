"""
My little Stack
"""
from typing import Any

stack = [] #переменная стек

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	print("Add element {} in stack".format(elem))

	global stack
	stack.append(elem)

	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack. If not elements - should return None.

	:return: popped element
	"""
	global stack
	if not stack:
		return None
	else:
		n = stack[-1]
		del stack[-1]
		return n


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it.

	:param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
	:return: peeked element or None if no element in this place
	"""
	print("Index:", ind)

	global stack
	if not stack:
		return None
	else:
		return stack[ind]


def clear() -> None:
    """
    Clear my stack
    :return: None
    """
    global stack
    stack = []
    return None

if __name__ == "__main__":
	push(1)
	push(2)
	push(3)
	print(stack)
	print(pop())
	print(peek(1))
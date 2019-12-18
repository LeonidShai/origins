def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""

	open_skobka = brackets_row.count("(")
	close_skobka = brackets_row.count(")")
	if open_skobka == close_skobka:
		return True
	else:
		return False

if __name__ == "__main__":
	print(check_brackets(""))
class Solution:
	# @param {string} s
	# @return {boolean}
	def isValid(self, s):
		stack = []
		match = {
			'}': '{',
			']': '[',
			')': '(',
		}
		for p in s:
			if p == '{' or p == '(' or p == '[':
				stack.append(p)
			else:
				if len(stack) == 0:
					return False
				if match[p] == stack[-1]:
					stack.pop(-1)
				else:
					return False 
		return len(stack) == 0

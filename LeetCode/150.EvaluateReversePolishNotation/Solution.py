import pdb
class Solution(object):
	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		pdb.set_trace()
		operands = []
		for i in range(len(tokens)):
			if not tokens[i] in ['+','-','*','/']:
				operands.append(int(tokens[i]))
			else:
				op2, op1 = operands.pop(), operands.pop()
				if tokens[i] == '+':
					rst = op2 + op1
				if tokens[i] == '-':
					rst = op1 - op2
				if tokens[i] == '*':
					rst = op1 * op2
				if tokens[i] == '/':
					rst = 1
					if op1 < 0: 
						op1 = -op1
						rst = -rst
					if op2 < 0:
						op2 = -op2
						rst = -rst
					rst *= op1 / op2
				operands.append(rst)
		rst = operands.pop()
		return rst 

if __name__ == '__main__':
	sol = Solution()
	cases = [["0", "3", "/"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]

	for case in cases:
		print sol.evalRPN(case)

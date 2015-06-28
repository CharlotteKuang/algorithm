from pdb import set_trace as st

class Solution:
	# @param {string} s
	# @return {integer}
	def calculate(self, s): 
		def operatingStacks(ns, os):
			# @param {integer} operand1
			# @param {integer} operand2
			# @param {string} operation
			# @return {integer}
			def cal(operand1, operand2, operation):
				if operation == '+': return operand1 + operand2
				if operation == '-': return operand1 - operand2
			num2, num1 = ns.pop(), ns.pop()
			return cal(num1, num2, os.pop())

		numStack, operandStack = [], []
		count, length, numMode = 0, len(s), True
		#st()
		while count < length:
			if s[count] in ['(', ')', ' ']:
				if s[count] == '(':
					operandStack.append('(')
					numMode = True
				if s[count] == ')':
					while operandStack[-1] != '(':
						numStack.append(operatingStacks(numStack, operandStack)) 
					operandStack.pop() #pop '('
					numMode = False 
				count += 1
				continue
			if numMode:
				c = count
				sign = 1
				if s[c] == '-':
					sign = -1
					c += 1
				num = 0
				while c < length and '0' <= s[c] <= '9':
					num = num * 10 + int(s[c]) 
					c += 1
				num = num * sign
				numStack.append(num)
				numMode = False
				count = c-1
			else:
				if len(operandStack) == 0 or operandStack[-1] == '(':
					operandStack.append(s[count])
				else:
					numStack.append(operatingStacks(numStack, operandStack)) 
					operandStack.append(s[count])
				numMode = True
			count += 1

		while operandStack:
			numStack.append(operatingStacks(numStack, operandStack)) 
		return numStack.pop()

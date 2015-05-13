import sys

class Solution:
	# @param {string} str
	# @return {integer}
	def strip(self, str):
		i = -1
		for c in str:
			if c != ' ':
				break
			i += 1
		return str[i+1:] 
	def stripBack(self, str):
		length = len(str)
		i = length
		for j in range(length):
			if str[length-j-1] != ' ':
				break
			i -= 1
		return str[0:i]

	# @param {string} str
	# @return {integer}
	def myAtoi(self, str):
		maxint = 2147483647
		minint = -2147483648
		s = self.strip(str)
		s = self.stripBack(s)
		if s == '': return 0
		sign = 1
		result = 0
		start = 0
		if s[start] == '+' or s[start] == '-':
			if s[start] == '-':
				sign = -1
			start += 1
		for i in range(start, len(s)):
			if not ('0' <= s[i] <= '9'):
				return result * sign
			result = result*10+(int(s[i]))
			if result > maxint:
				if sign > 0: return maxint
				else: return minint
		return result * sign

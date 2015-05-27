class Solution:
	def __init__(self):
		self.digitsMap = [
			[], [], 
			['a','b','c'], 
			['d','e','f'], 
			['g','h','i'],
			['j','k','l'],
			['m','n','o'],
			['p','q','r','s'],
			['t','u','v'],
			['w','x','y','z'],
		]

	# @param {string} digits
	# @return {string[]}
	def letterCombinations(self, digits):
		if digits == '': return []
		result = ['']	
		for d in digits:
			length = len(result)
			while length:
				tmp = result.pop(0)
				for letter in self.digitsMap[int(d)]:
					result.append(tmp+letter)
				length -= 1
		return result

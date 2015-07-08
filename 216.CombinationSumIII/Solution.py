import copy
import pdb
class Solution:
	def findCom(self, k, n, combination, s):
		#pdb.set_trace()
		if len(combination) == k:
			if s == n:
				return [copy.copy(combination)]
			else: return []
		else:
			result = []
			last = 1
			if len(combination): last = combination[-1]
			for i in range(last, 10):
				if s + i <= n:
					combination.append(i)
					tmp = self.findCom(k, n, combination, s + i)
					result += tmp
					combination.pop()
			return result
	# @param {integer} k
	# @param {integer} n
	# @return {integer[][]}
	def combinationSum3(self, k, n):
		return self.findCom(k, n, [], 0)


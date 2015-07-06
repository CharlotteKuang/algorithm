class Solution:
	# @param {integer} n
	# @return {boolean}
	def isPowerOfTwo(self, n):
		result = n
		while result > 0 and result & 1 == 0:
			result >>= 1
		return result == 1

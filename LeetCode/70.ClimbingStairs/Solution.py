class Solution:
	# @param {integer} n
	# @return {integer}
	def climbStairs(self, n):
		steps = [0] * (n+2)
		if n >= 1: 
			steps[2] = 1
		if n >= 2: steps[3] = 2
		for i in range(4, len(steps)):
			steps[i] = steps[i-1] + steps[i-2]
		return steps[-1]



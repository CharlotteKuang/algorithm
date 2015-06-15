from pdb import set_trace as debug

class Solution:
	# @param {integer} n
	# @return {integer}
	def numTrees(self, n): 
		dp = [1, 1]
		#debug()
		for i in range(2, n+1):
			treeCount = 0
			for j in range(1, i+1):
				treeCount += dp[j-1]*dp[i-j]
			dp.append(treeCount)
		return dp[n]

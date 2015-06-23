from pdb import set_trace as debug

class Solution:
	# @param {string} s1
	# @param {string} s2
	# @param {string} s3
	# @return {boolean}
	def isInterleave(self, s1, s2, s3): 
		if len(s1)+len(s2) != len(s3): return False
		if len(s1) == 0: return s2 == s3
		if len(s2) == 0: return s1 == s3

		dp = []
		for i in range(len(s2)+1):
			dp.append([False]*(len(s1)+1)) 
		dp[0][0] = False

		for i in range(1,len(s1)+1):
			dp[0][i] = s1[0:i] == s3[0:i]
		for i in range(1,len(s2)+1):
			dp[i][0] = s2[0:i] == s3[0:i]
		for i in range(1,len(s2)+1):
			for j in range(1,len(s1)+1):
				if dp[i-1][j]: dp[i][j] = s2[i-1] == s3[i+j-1]
				if dp[i][j-1]: dp[i][j] = s1[j-1] == s3[i+j-1]
		return dp[len(s2)][len(s1)] 

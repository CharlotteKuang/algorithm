import pdb
class Solution(object):
	def minDistance(self, word1, word2):
		if word1 == word2: return 0
		if not word1: return len(word2)
		if not word2: return len(word1)
		
		l1, l2 = len(word1), len(word2)
		dp = range(l2+1)
		for i in range(1, 1+l1):
			for j in range(1+l2):
				if j == 0:
					dp_ij = dp[0]
					dp[0] = i
				else:
					dp_ij_bak = dp[j]
					dp[j] = min(dp[j-1] + 1,
						dp[j] + 1,
						dp_ij + (0 if (word1[i-1] == word2[j-1]) else 1))
					dp_ij = dp_ij_bak
		return dp[-1]
				
	def minDistance_tmp(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		""" 
		#trival case
		if word1 == word2: return 0
		if not word1: return len(word2)
		if not word2: return len(word1)

		l1, l2 = len(word1), len(word2)
		dp = [[0 for i in range(l1+1)] for j in range(l2+1)]
		
		#init dp
		for i in range(l2):
			dp[i][l1] = l2 - i
		for j in range(l1):
			dp[l2][j] = l1 - j

		#run dp
		for i in range(l2):
			pos2 = l2-i-1
			for j in range(l1): 
				pos1 = l1-j-1
				if word1[pos1] == word2[pos2]:
					dp[pos2][pos1] = dp[pos2+1][pos1+1]
				else:
					dp[pos2][pos1] = 1 + min(dp[pos2][pos1+1], dp[pos2+1][pos1], dp[pos2+1][pos1+1])
		return dp[0][0]

if __name__ == '__main__':
	sol = Solution()
	testCases = [("sea", "ate"), ('abc', 'acef'), ('a', 'a'), ('abc', 'ddd'), ('abc', ''),
		("sea", "ate")]
	print sol.minDistance('ab', 'a')
	for test in testCases:
		print sol.minDistance_tmp(test[0], test[1]), sol.minDistance(test[0], test[1])

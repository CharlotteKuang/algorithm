import pdb
class Solution(object):
	def minCut(self, s):
		"""
		:type s: str
		:rtype: int
		""" 
		l = len(s)
		if l <= 1: return 0

		isPalindrome = [[False for i in range(l)] for i in range(l)] 
		minCuts = []

		for i in range(l+1):
			minCuts.append(i-1)

		for i in range(1, l):
			for j in range(i, -1, -1):
				if s[i] == s[j] and (i-j <= 2 or isPalindrome[j+1][i-1]):
					isPalindrome[j][i] = True
					minCuts[i+1] = min(minCuts[i+1], minCuts[j]+1)

		return minCuts[l]

if __name__ == '__main__':
	sol = Solution()

	cases = ['aab', 'abbaaac', '', 'abba']
	for case in cases:
		print sol.minCut(case)

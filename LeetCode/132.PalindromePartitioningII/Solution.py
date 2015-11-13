import pdb
class Solution(object):
	def minCut(self, s):
		#reference: https://leetcode.com/discuss/47140/two-versions-given-one-28ms-one-manancher-like-algorithm-10
		"""
		:type s: str
		:rtype: int
		""" 
		l = len(s)
		if l <= 1: return 0

		minCuts = []

		for i in range(l+1):
			minCuts.append(i-1)

		for i in range(1, l):
			for j in range(0, l-i):
				if i+j >= l or i-j < 0 or s[i-j] != s[i+j]: break
				minCuts[i+j+1] = min(minCuts[i+j+1], minCuts[i-j]+1)
			for j in range(0, l-i):
				if i+j >= l and i-j-1 < 0 or s[i-j-1] != s[i+j]: break
				minCuts[i+j+1] = min(minCuts[i+j+1], minCuts[i-j-1]+1)
		return minCuts[l]

if __name__ == '__main__':
	sol = Solution()

	cases = ['aab', 'abbaaac', '', 'abba']
	for case in cases:
		print sol.minCut(case)

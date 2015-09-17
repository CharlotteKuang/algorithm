class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		""" 
		l = len(s)
		if l == 0 or s[0] == '0': return 0

		dp = [0 for i in range(l)]
		intValues = [int(n) for n in s]
		dp[0] = 1
		if l >= 2:
			if intValues[1] > 0: dp[1] = 1
			if 10 <= intValues[0]*10+intValues[1] <= 26:
				dp[1] += 1 

		for i in range(2, l):
			if intValues[i] == 0:
				if intValues[i-1] in [1,2]:
					dp[i] += dp[i-2]
				continue
			dp[i] += dp[i-1]	
			if 10 <= intValues[i-1]*10+intValues[i] <= 26:
				dp[i] += dp[i-2]
		print dp
		return dp[-1]

if __name__ == '__main__':
	sol = Solution()

	cases = ['101', '12', '123201', '42925132', '4', '', '10', '123401']
	for case in cases:
		print sol.numDecodings(case)

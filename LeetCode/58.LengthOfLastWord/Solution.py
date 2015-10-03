class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		l = len(s)
		c = 0
		flag = False
		for i in range(l):
			if s[l-i-1] == ' ':
				if flag: break
				else: continue
			flag = True
			c += 1
		return c

if __name__ == '__main__':
	sol = Solution()

	cases = ['a ', 'Hello World', '  b  ']

	for c in cases:
		print sol.lengthOfLastWord(c)

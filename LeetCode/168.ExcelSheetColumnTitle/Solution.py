class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		result = []
		_Anum = ord('A') 
		while n > 0:
			result.insert(0, chr(_Anum + (n-1) % 26))
			n = (n-1) / 26
		return ''.join(result)

if __name__ == '__main__':
	sol = Solution()
	for i in range(1, 53):
		print sol.convertToTitle(i)

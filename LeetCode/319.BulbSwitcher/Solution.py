class Solution(object):
	def bulbSwitch(self, n):
		"""
		:type n: int
		:rtype: int
		""" 

		start = 0
		while True:
			if (start+1) * (start+1) <= n:
				start += 1
			else: 
				break
		return start

if __name__ == '__main__':
	sol = Solution()
	for i in range(1, 1000):
		print i, sol.bulbSwitch(i)
	#print 999999, sol.bulbSwitch(999999)

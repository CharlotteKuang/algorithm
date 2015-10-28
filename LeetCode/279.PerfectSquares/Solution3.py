import pdb
from math import sqrt
haha = {}
class Solution(object):
	def numSquares(self, n):
		global haha
		if n in haha:
			return haha[n]

		squares = []
		for i in range(1, 100):
			squares.append(i*i)
			haha[i*i] = 1
				
		for count in range(1, 6):
			tmp = []
			for i in squares:
				for j in haha:
					if not i+j in haha:
						tmp.append(i+j)
			for t in tmp:
				if not t in haha:
					haha[t] = count+1
			count += 1 
		"""
		:type n: int
		:rtype: int
		""" 
		return haha[n]
if __name__ == '__main__':
	for i in range(1, 10000):
		sol = Solution()
		print i, sol.numSquares(i)

import random
import pdb
#https://leetcode.com/discuss/58186/elegant-c-solution-o-n-space-time-with-detailed-explanation
class Solution(object):
	def __init__(self):
		self.__cache__ = [1]
		self.visited = {}
		self.curPos = 0
	def nthUglyNumber_my(self, n): 
		"""
		:type n: int
		:rtype: int
		""" 
		#pdb.set_trace()
		if self.curPos >= n: return self.__cache__[n-1]

		cover = 1
		while cover < n*3: 
			cover *= 3

		count = len(self.__cache__)
		p = self.curPos

		while count < cover:
			cur = self.__cache__[p]
			for i in [2,3,5]:
				if not cur*i in self.visited:
					mul = cur*i
					count += 1
					self.visited[mul] = True
					self.__cache__.append(mul)
			p += 1

		self.curPos = p  
		self.__cache__.sort()
		return self.__cache__[n-1]

	def nthUglyNumber(self, n):
		i, j, k = 0, 0, 0
		rst = [1]
		#pdb.set_trace()
		while len(rst) < n:
			c2, c3, c5 = rst[i]*2, rst[j]*3, rst[k]*5
			minC = min(c2, c3, c5)
			if minC == c2: 
				i += 1
			elif minC == c3:
				j += 1
			else:
				k += 1
			rst.append(minC)
		return rst[n-1]
if __name__ == '__main__': 
	sol = Solution()
	for i in range(0, 500):
		n = random.randint(1, 800000)
		print n, sol.nthUglyNumber(n)

import copy
import pdb
class Solution(object):
	def combine_helper(self, n, k, l):
		#pdb.set_trace()
		if len(l) == k:
			self.combine_list.append(copy.copy(l))
			return
		head = 0
		if len(l) > 0:
			head = l[-1]
		for i in range(head+1, n+1):
			l.append(i)
			self.combine_helper(n, k, l)
			l.pop()
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		""" 
		self.combine_list = []
		self.combine_helper(n, k, [])
		return self.combine_list

if __name__ == '__main__':
	sol = Solution()
	print sol.combine(4, 2)
	print sol.combine(3, 1)
	print sol.combine(5, 2)
	print sol.combine(6, 3)

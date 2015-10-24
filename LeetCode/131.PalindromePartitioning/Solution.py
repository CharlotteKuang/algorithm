import pdb
import copy
class Solution(object):
	def isPalindrome(self, s, head, tail):
		while head < tail:
			if s[head] != s[tail]: return False
			head += 1
			tail -= 1
		return True
	def helper(self, s, start, end):
		if start > end: return [[""]]
		if start == end:
			return [[s[start:start+1]]]
		rst = []
		if not start in self.record:
			self.record[start] = {} 
		if not end in self.record[start]:
			self.record[start][end] = []
		for i in range(start, end+1):
			if self.isPalindrome(s, start, i):
				if i+1 in self.record and end in self.record[i+1]:
					partRst = self.record[i+1][end]
				else:
					partRst = self.helper(s, i+1, end)
				first = s[start:i+1]
				for par in partRst:
					if par[-1] == "": par.pop()
					newList = [first] + copy.copy(par)
					self.record[start][end].append(newList)
					rst.append(newList)
		return rst
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		""" 
		self.record = {}
		return self.helper(s, 0, len(s)-1)

if __name__ == '__main__':
	sol = Solution() 
	cases  = ["aa", "aab", "aabb", ""]
	for case in cases:
		print sol.partition(case)
		print sol.record

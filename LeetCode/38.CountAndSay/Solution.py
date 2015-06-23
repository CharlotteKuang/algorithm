import pdb
class Solution:
	def __init__(self):
		self.__say__ = ['1']
	# @param {integer} n
	# @return {string}
	def countAndSay(self, n):
		if len(self.__say__) >= n: return self.__say__[n-1]
		for i in range(len(self.__say__), n):
			say= self.__say__[-1]
			pos, last = 0, ''
			nextSay = ''
			while pos < len(say):
				if not last: last = say[pos]
				count = 0
				while pos < len(say) and say[pos] == last:
					pos += 1
					count += 1
				nextSay += str(count) + last
				last = ''
			self.__say__.append(nextSay)
		return self.__say__[n-1]

if __name__ == '__main__':
	solution = Solution()
	for i in range(1, 10):
		print solution.countAndSay(i)

class Solution:
	# @param {string} s
	# @param {string} t
	# @return {boolean}
	def isIsomorphic(self, s, t):
		transformDict = {}						        
		length = len(s)	
		for i in range(length):
			if not s[i] in transformDict:
				transformDict[s[i]] = t[i]
			else:
				if transformDict[s[i]] != t[i]:
					return False
		transformDict = {}						        
		length = len(s)	
		for i in range(length):
			if not t[i] in transformDict:
				transformDict[t[i]] = s[i]
			else:
				if transformDict[t[i]] != s[i]:
					return False
		return True


def main():
	test = Solution()
	testCases = [
		('paper', 'title'),
		('egg', 'add'),
		('foo', 'bar'),
		('ab', 'aa'),
	]
	for testCase in testCases:
		print testCase[0], ' ', testCase[1]
		print test.isIsomorphic(testCase[0], testCase[1])

if __name__ == '__main__':
	main()

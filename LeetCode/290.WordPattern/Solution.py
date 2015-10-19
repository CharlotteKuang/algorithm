class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		strArr = str.split(' ')
		if len(strArr) != len(pattern): return False
		count = 0
		strDict = {}
		for p in pattern:
			if not p in strDict:
				strDict[p] = strArr[count]
			else:
				if strDict[p] != strArr[count]:
					return False
			count += 1
		count = 0
		pDict = {}
		for s in strArr:
			if not s in pDict:
				pDict[s] = pattern[count]
			else:
				if pDict[s] != pattern[count]:
					return False
			count += 1
		return True

if __name__ == '__main__':
	sol = Solution()
	#pattern, string = "abba","dog dog dog dog"
	pattern = "abba"
	string = "dog cat cat dog"
	print sol.wordPattern(pattern, string)

import pdb
class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		#pdb.set_trace()
		result = min(len(s), 1)
		pointer = 0
		charDict = {}
		for i in range(len(s)):
			if s[i] in charDict: 
				if charDict[s[i]] < pointer:
					charDict[s[i]] = i
				else:
					result = max(result, i-pointer)
					pointer = charDict[s[i]] + 1
			charDict[s[i]] = i
		return max(result, len(s)-pointer)

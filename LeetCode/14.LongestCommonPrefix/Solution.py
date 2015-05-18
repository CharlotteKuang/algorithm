class Solution:
	# @param {string[]} strs
	# @return {string}
	def longestCommonPrefix(self, strs):
		if len(strs) == 0: return ''
		if len(strs) == 1: return strs[0] 
		result = []
		i = 0
		flag = True 
		while flag:
			commonChar = ''
			for s in strs:
				if i >= len(s):
					flag = False
					break
				if commonChar == '':
					commonChar = s[i]
				else:
					if commonChar != s[i]:
						flag = False
						break
			if flag:
				i += 1
				result.append(commonChar)
		return ''.join(result)

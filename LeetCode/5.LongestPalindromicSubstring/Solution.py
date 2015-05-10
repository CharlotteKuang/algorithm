import pdb

class Solution:
	# @param {string} s
	# @return {string}
	def addBoundaries(self, s):
		result = '|'
		for c in s:
			result += c + '|'
		return result
	
	# @param {string} s
	# @return {string}
	def removeBoundaries(self, s):
		result = ''
		for i in range((len(s)-1) / 2):
			result += s[i*2+1]
		return result

	# @param {string} s
	# @return {string}
	def longestPalindrome(self, s):
		auxiliary = self.addBoundaries(s)
		length = len(auxiliary)
		p = [0] * length
		c = 0
		r = 0
		m = 0
		n = 0
		#pdb.set_trace()
		for i in range(1, length):
			if i > r: 
				m = i - 1
				n = i + 1
			else:
				i2 = 2 * c - i
				if i2 < 0:
					m = -1
				else:
					if p[i2] < r - i:
						p[i] = p[i2]
						m = -1
					else:
						p[i] = r - i
						n = r + 1
						m = 2 * i - n
			while m >= 0 and n < length and auxiliary[m] == auxiliary[n]:
				p[i] += 1
				m -= 1
				n += 1
			if p[i] + i > r:
				c = i
				r = p[i] + i
		c = 0
		maxLen = 0
		for i in range(0, length):
			if p[i] > maxLen:
				c = i
				maxLen = p[i]
		targetStr = auxiliary[c - maxLen : c + maxLen + 1]
		return self.removeBoundaries(targetStr)

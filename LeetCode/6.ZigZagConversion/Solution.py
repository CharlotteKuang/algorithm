import pdb
class Solution:
	# @param {string} s
	# @param {integer} numRows
	# @return {string}
	def convert(self, s, numRows):
		length = len(s)
		if numRows >= length or numRows == 1:
			return s
		resultArr = [''] * length
		zigSize = numRows * 2 - 2
		if length  % zigSize == 0:
			numZig = length / zigSize
		else:
			numZig = length / zigSize + 1
		c = 0
		for i in range(numZig):
			resultArr[c] = s[i * zigSize]
			c += 1
		for i in range(1, numRows-1):
			count = 0
			while True:
				if count % 2 == 0:
					tmp = count / 2 * zigSize + i
				else:
					tmp = count / 2 * zigSize + zigSize - i
				if tmp >= length:
					break
				resultArr[c] = s[tmp]
				c += 1
				count += 1

		for i in range(numZig):
			tmp = i * zigSize + numRows - 1
			if tmp >= length:
				break
			resultArr[c] = s[tmp]
			c += 1
		return ''.join(resultArr)

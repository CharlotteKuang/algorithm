class Solution:
	# @param {integer} numRows
	# @return {integer[][]}
	def generate(self, numRows):
		result = []
		for i in range(1, numRows+1):
			row = []
			for j in range(1, i+1):
				if j == 1 or j == i: row.append(1)
				elif i > 1:
					row.append(result[-1][j-2]+result[-1][j-1])
			result.append(row)
		return result

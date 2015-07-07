class Solution:
	# @param {integer} rowIndex
	# @return {integer[]}
	def getRow(self, rowIndex):
		if rowIndex <= 1: return [1]*(rowIndex+1)
		result = [1,1] 
		for i in range(2, rowIndex+1):
			tmp1 = result[0]
			for j in range(1, i):
				tmp2 = result[j]
				result[j] = result[j] + tmp1
				tmp1 = tmp2
			result.append(1)
		return result

import pdb
class Solution:
	# @param {integer[][]} matrix
	# @return {void} Do not return anything, modify matrix in-place instead.
	def rotate(self, matrix):
		n = len(matrix)
		count = 0
		#pdb.set_trace()
		for count in range(n/2):
			size = n - count*2
			settlePoints = [
				(count, count),
				(count, n-count-1),
				(n-count-1, n-count-1),
				(n-count-1, count),
			]
			tmp = 0
			for i in range(size-1):
				curr, curc = settlePoints[0][0], settlePoints[0][1]+i
				nextr, nextc = settlePoints[1][0]+i, settlePoints[1][1]
				tmp1 = matrix[nextr][nextc]
				matrix[nextr][nextc] = matrix[curr][curc]

				nextr, nextc = settlePoints[2][0], settlePoints[2][1]-i
				tmp2 = matrix[nextr][nextc]
				matrix[nextr][nextc] = tmp1

				nextr, nextc = settlePoints[3][0]-i, settlePoints[3][1]
				tmp3 = matrix[nextr][nextc]
				matrix[nextr][nextc] = tmp2 

				matrix[curr][curc] = tmp3


import pdb
class Solution(object):
	def minimumTotal(self, triangle):
		pdb.set_trace()
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		if len(triangle) == 0:
			return 0
		if len(triangle) == 1:
			return triangle[0][0]
		minTotal = []
		rows = len(triangle)
		for i in range(rows+1):
			minTotal.append([])
			for j in range(i+1):
				minTotal[-1].append(0)
		for i in range(rows):		
			minTotal[rows-1][i] = triangle[rows-1][i]
		for i in range(rows):
			r_idx = rows - i - 1
			for j in range(r_idx+1):
				minTotal[r_idx][j] = triangle[r_idx][j] + min(minTotal[r_idx+1][j], minTotal[r_idx+1][j+1])
		return minTotal[0][0]

if __name__ == '__main__':
	sol = Solution()
	triangle = [[-1],[-2,-3]]
	print sol.minimumTotal(triangle)

	triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
	print sol.minimumTotal(triangle) 

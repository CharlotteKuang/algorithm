import pdb
class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if len(grid) == 0: return 0
		if len(grid[0]) == 0: return 0
		
		rows = len(grid)
		cols = len(grid[0])
		
		#init dp
		dp = [[0 for n in range(cols)] for m in range(rows)]
		dp[0][0] = grid[0][0]
		#pdb.set_trace()	
		for i in range(1, cols):
			dp[0][i] = grid[0][i]+dp[0][i-1]
		for j in range(1, rows):
			dp[j][0] = grid[j][0]+dp[j-1][0]
		#dp
		for i in range(1, rows):
			for j in range(1, cols):
				dp[i][j] = grid[i][j]+min(dp[i-1][j], dp[i][j-1])
		return dp[-1][-1]

if __name__ == '__main__':
	sol = Solution()
	case = [[1,2,5],[3,2,1]]
	print sol.minPathSum(case)

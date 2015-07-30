from pdb import set_trace as db

class Solution:
	# @param {integer[][]} obstacleGrid
	# @return {integer}
	def uniquePathsWithObstacles(self, obstacleGrid):
		if len(obstacleGrid) == 0: return 0
		if len(obstacleGrid[0]) == 0: return 0

		m = len(obstacleGrid)
		n = len(obstacleGrid[0])

		if obstacleGrid[m-1][n-1]: return 0

		path_count = []
		for i in range(m):
			path_count.append([0] * n)

		#missing this statement
		if not obstacleGrid[0][0]: path_count[0][0] = 1	

		#missing thie statement
		for i in range(1, m):
			if obstacleGrid[i-1][0]: 
				break
			path_count[i][0] = 1 
		for j in range(1, n):
			if obstacleGrid[0][j-1]: 
				break
			path_count[0][j] = 1

		for i in range(1, m):
			for j in range(1, n): 
				left_paths = 0
				top_paths = 0
				if not obstacleGrid[i][j-1]: left_paths = path_count[i][j-1]
				if not obstacleGrid[i-1][j]: top_paths = path_count[i-1][j]
				path_count[i][j] = left_paths + top_paths
		return path_count[m-1][n-1]

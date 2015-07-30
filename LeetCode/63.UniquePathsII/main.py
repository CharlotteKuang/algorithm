from Solution import Solution

if __name__ == '__main__':
	solution = Solution() 
		
	obs = [[0,1]]
	print solution.uniquePathsWithObstacles(obs) 
	obs = [[0,0,0],[0,1,0],[0,0,0]]
	print solution.uniquePathsWithObstacles(obs) 
	obs = [[1,0,0],[0,1,0],[0,0,0]]
	print solution.uniquePathsWithObstacles(obs) 
	obs = [[0,0,0],[0,0,0],[0,0,0]]
	print solution.uniquePathsWithObstacles(obs) 
	obs = [[0,0,0],[1,0,0],[0,0,0]]
	print solution.uniquePathsWithObstacles(obs) 
	#wrong answer
	obs = [[0]]
	print solution.uniquePathsWithObstacles(obs) 

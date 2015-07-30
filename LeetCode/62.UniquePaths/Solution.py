from pdb import set_trace as db

class Solution:
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def uniquePaths(self, m, n): 
		if m == 0 or n == 0: return 0
		path_count = []
		for i in range(m):
			path_count.append([1] * n)
		for i in range(1, m):
			for j in range(1, n): 
				left_paths = 0
				top_paths = 0
				sum_paths = 0
				try: 
					left_paths = path_count[i][j-1]
				except IndexError:
					pass
				try: 
					top_paths = path_count[i-1][j]
				except IndexError:
					pass
				#path_count[i][j] += left_paths + top_paths #wrong!
				path_count[i][j] = left_paths + top_paths

		return path_count[m-1][n-1]

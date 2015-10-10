class Solution:
	def isValid(self, x, y):
		return x >= 0 and x < self.m and y >= 0 and y < self.n
	def calculateCellMinimumHP(self, curGrid, nextNeedHealth):
		if curGrid <= 0:
			return max(nextNeedHealth,1) - curGrid
		else:
			if curGrid >= nextNeedHealth: return 0
			else: return nextNeedHealth - curGrid
	# @param dungeon, a list of lists of integers
	# @return a integer
	def calculateMinimumHP(self, dungeon):
		self.m = m = len(dungeon)
		self.n = n = len(dungeon[0])
		maxInt = 100000
		health = []
		for i in range(0, m):
			health.append([1]*n)
		rows = range(0, m)
		cols = range(0, n)
		rows.reverse()
		cols.reverse()
		health[m-1][n-1] = 1 - min(0, dungeon[m-1][n-1])
		#pdb.set_trace()
		for i in rows:
			for j in cols:
				if i == m-1 and j == n-1: continue
				if not self.isValid(i, j+1): 
					rightMinimumHealth = maxInt
				else: 
					rightMinimumHealth = self.calculateCellMinimumHP(dungeon[i][j], health[i][j+1]) 
				if not self.isValid(i+1, j):
					downMinimumHealth = maxInt
				else:
					downMinimumHealth = self.calculateCellMinimumHP(dungeon[i][j], health[i+1][j])
				health[i][j] = min(rightMinimumHealth, downMinimumHealth)
		return max(1,health[0][0]) 


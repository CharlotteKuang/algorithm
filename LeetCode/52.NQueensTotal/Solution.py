class Solution:
	# @return generator
	def solve(self, num, current):
		if len(current) == num:
			return 1
		else:
			row = len(current)
			solutions = 0
			for i in range(num): # i for the col candidates of row[len(current)]
				flag = True
				for j in range(row): #current[j] for col of row[j]
					if i == current[j] or i == current[j] - j + row or i == j + current[j] - row:
						flag = False
						break
				if flag:
					solutions += self.solve(num, current + [i])
			return solutions

	# @return a list of lists of string
	def totalNQueens(self, n):
		return self.solve(n, [])		

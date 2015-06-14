from pdb import set_trace as debug
import copy

class Solution:
	# @return generator
	def solve(self, num, current):
		if len(current) == num:
			board = []
			for i in range(num):
				board.append('.' * current[i] + 'Q' + '.' * (num-current[i]-1))
			yield board 
		else:
			row = len(current)
			for i in range(num): # i for the col candidates of row[len(current)]
				flag = True
				for j in range(row): #current[j] for col of row[j]
					if i == current[j] or i == current[j] - j + row or i == j + current[j] - row:
						flag = False
						break
				if flag:
					for subSolution in self.solve(num, current + [i]):
						yield subSolution

	# @return a list of lists of string
	def solveNQueens(self, n):
		result = []
		for solution in self.solve(n, []):		
			result.append(solution)
		return result

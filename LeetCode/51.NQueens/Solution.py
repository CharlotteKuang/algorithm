from pdb import set_trace as debug
import copy

class Solution:
	# @return generator
	def solve(self, n, current):
		if len(current) == n:
			board = []
			for i in range(n):
				board.append('.' * current[i] + 'Q' + '.' * (n-current[i]-1))
			yield board 
		else:
			row = len(current)
			for col in range(n): # i for the col candidates of row[len(current)]
				flag = True
				if self.__colBit & (1 << col): flag = False
				if self.__45Bit & (1 << (row + col)): flag = False
				if self.__135Bit & (1 << (n - row + col - 1)): flag = False
				if flag:
					tmp1, tmp2, tmp3 = self.__colBit, self.__45Bit, self.__135Bit
					self.__colBit |= 1 << col
					self.__45Bit |= 1 << (row + col)
					self.__135Bit |= 1 << (n - row + col - 1)
					for subSolution in self.solve(n, current + [col]):
						yield subSolution
					self.__colBit = tmp1
					self.__45Bit = tmp2
					self.__135Bit = tmp3

	# @return a list of lists of string
	def solveNQueens(self, n):
		result = []
		self.__colBit = 0
		self.__45Bit = 0
		self.__135Bit = 0
		for solution in self.solve(n, []):		
			result.append(solution)
		return result

import pdb
class Solution:
	def recursiveSolve(self, board, rowHash, colHash, gridHash, count, i, j):
		if count == 81: return True	
		bits = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
		if board[i][j] != '.':
			if j == 8: nextI, nextJ = i + 1, 0
			else: nextI, nextJ = i, j + 1
			return self.recursiveSolve(board, rowHash, colHash, gridHash, count, nextI, nextJ)

		for num in range(1, 10):
			bit = bits[num]
			grid = i / 3 * 3 + j / 3
			if not rowHash[i] & bit and not colHash[j] & bit and not gridHash[grid] & bit:
				board[i][j] = str(num)
				bit = bits[num]
				rowHash[i] |= bit
				colHash[j] |= bit
				gridHash[grid] |= bit

				if j == 8: nextI, nextJ = i + 1, 0
				else: nextI, nextJ = i, j + 1
				if self.recursiveSolve(board, rowHash, colHash, gridHash, count+1, nextI, nextJ):
					return True
				else:
					rowHash[i] &= ~bit
					colHash[j] &= ~bit
					gridHash[grid] &= ~bit
					board[i][j] = '.'

	# @param {character[][]} board
	# @return {void} Do not return anything, modify board in-place instead.
	def solveSudoku(self, board): 
		#grid mark
		rowHash = [0] * 9
		colHash = [0] * 9
		gridHash = [0] * 9
		bits = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

		#candidates for 81 grids
		candidates = []
		filledCount = 0

		#init candidates and set grid mark hash
		for i in range(9):
			candidates.append([])
			for j in range(9):
				candidates[-1].append([])
				if board[i][j] != '.':
					val = int(board[i][j])
					grid = i / 3 * 3 + j / 3
					bit = bits[val]
					rowHash[i] |= bit
					colHash[j] |= bit
					gridHash[grid] |= bit
					filledCount += 1

		#filling sudoku
		flag = True 
		while flag:
			flag = False
			for i in range(9):
				for j in range(9):
					grid = i / 3 * 3 + j / 3
					if board[i][j] == '.':
						count = 0
						target = '.'
						for num in range(1, 10):
							bit = bits[num]
							if not rowHash[i] & bit and not colHash[j] & bit and not gridHash[grid] & bit:
								count += 1
								target = num 
						if count == 1:
							flag = True
							board[i][j] = str(target)
							bit = bits[target]
							rowHash[i] |= bit
							colHash[j] |= bit
							gridHash[grid] |= bit
							filledCount += 1
		if filledCount < 81:
			self.recursiveSolve(board, rowHash, colHash, gridHash, filledCount, 0, 0)

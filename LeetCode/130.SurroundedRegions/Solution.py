class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		""" 
		try:
			row = len(board)
			col = len(board[0])

			def valid(x, y):
				return 0 <= x < row and 0 <= y < col
			def is_border(x, y):
				return 0 == x or x == row-1 or y == 0 or y == col-1

			visited = [[False for n in range(col)] for m in range(row)]
			directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
			for i in range(row): #1
				for j in range(col): #2
					if board[i][j] != 'O' or visited[i][j]: continue
					q = [(i,j)]
					flip = True
					flipCells = [(i, j)]
					visited[i][j] = True
					if is_border(i, j): flip = False
					while len(q): #3
						cur = q.pop(0)
						for d in directions: #4
							new_i = cur[0] + d[0]
							new_j = cur[1] + d[1]
							if valid(new_i, new_j) and board[new_i][new_j] == 'O' and not visited[new_i][new_j]: #5
								visited[new_i][new_j] = True
								q.append((new_i, new_j))
								flipCells.append((new_i, new_j))
								if flip and is_border(new_i, new_j): #6
									flip = False
					if flip:
						for pos in flipCells:
							board[pos[0]][pos[1]] = 'X'
		except IndexError:
			pass

if __name__ == '__main__':
	test = [
		['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X'],
		['X', 'X', 'O', 'X'], 
		['X', 'O', 'X', 'X'],
	]
	sol = Solution()

	sol.solve(test)

	print test

	test = [
		['X', 'X', 'X', 'X'],
		['X', 'X', 'X', 'X'],
		['X', 'X', 'O', 'X'], 
		['X', 'O', 'X', 'X'],
	] 
	sol.solve(test)

	print test

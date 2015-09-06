import pdb
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

			visited = [[False for n in range(col)] for m in range(row)]
			directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
			def mark_non_surrounded_region(i, j):
				q = [(i,j)]
				visited[i][j] = True
				board[i][j] = '-'
				while len(q): #3
					cur = q.pop(0)
					for d in directions: #4
						new_i = cur[0] + d[0]
						new_j = cur[1] + d[1]
						if valid(new_i, new_j) and board[new_i][new_j] == 'O' and not visited[new_i][new_j]: #5
							board[new_i][new_j] = '-'
							visited[new_i][new_j] = True
							q.append((new_i, new_j))

			for i in [0, row-1]: #1
				for j in range(col): #2
					if board[i][j] == 'O' and not visited[i][j]:
					    mark_non_surrounded_region(i, j)
			for i in range(row): #1
				for j in [0, col-1]: #2
					if board[i][j] == 'O' and not visited[i][j]:
					    mark_non_surrounded_region(i, j)
			for i in range(row):
				for j in range(col):
					if board[i][j] == '-': board[i][j] = 'O'
					else: board[i][j] = 'X'
		except IndexError:
			pass
if __name__ == '__main__': 
	sol = Solution()
	test = [['O', 'O'],['O','O']]
	sol.solve(test)
	print test

	test = [
		['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X'],
		['X', 'X', 'O', 'X'], 
		['X', 'O', 'X', 'X'],
	]

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

class Solution(object):
	def trace(self, board, ordinate, word, pos, visited):
		if pos == len(word):
			return True
		else:
			dirs = [(0, -1),(0, 1),(1, 0),(-1, 0)]
			for d in dirs:
				r = ordinate[0] + d[0]
				c = ordinate[1] + d[1]
				if not (0 <= r < len(board)) or not (0 <= c < len(board[0])): continue
				if board[r][c] == word[pos] and not visited[r][c]:
					visited[r][c] = True
					traceRst = self.trace(board, (r,c), word, pos + 1, visited)
					if traceRst: return True
					visited[r][c] = False 
			return False
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		""" 
		if(len(board) == 0 or len(board[0]) == 0):
			return len(word) == 0

		visited = []
		wordMap = {}
		for i in range(len(board)):
			visited.append([])
			for j in range(len(board[i])):
				visited[-1].append(False)
				if not board[i][j] in wordMap:
					wordMap[board[i][j]] = 0
				wordMap[board[i][j]] += 1

		for i in word:
			if not i in wordMap: return False
			wordMap[i] -= 1
			if wordMap[i] < 0: return False

		for i in range(len(board)): 
			for j in range(len(board[i])):
				if board[i][j] == word[0]:
					visited[i][j] = True
					traceRst = self.trace(board, (i, j), word, 1, visited)
					visited[i][j] = False 
					if traceRst: return True
		return False

if __name__ == '__main__':
	sol = Solution()
	board = [
		['A','B','C','E'],
		['S','F','C','S'],
		['A','D','E','E'],
	]
	print sol.exist(["aaa","abb","abb","bbb","bbb","aaa","bbb","abb","aab","aba"], "aabaaaabbb")
	print sol.exist(["aaaa","aaaa","aaaa","aaaa","aaab"], "aaaaaaaaaaaaaaaaaaaa")
	print sol.exist(board, 'ABCCED')
	print sol.exist(board, 'SEE')
	print sol.exist(board, 'ABCB')

class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		if n == 0: return []
		matrix = []
		for	i in range(n):
			matrix.append([])
			for j in range(n):
				matrix[-1].append(0)
		self.spiralOrder(n, matrix)
		return matrix
	def spiralOrder(self, n, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return []
		row = n
		col = n
		
		top = 0 
		bottom = row - 1
		right = col - 1
		left = 0

		pos = (0, 0)
		border = [top, right, bottom, left]
		diff = (1, -1, -1, 1)
		directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
		cur_dir = 1
		count = 0
		
		result = []
		while count < row * col:
			matrix[pos[0]][pos[1]] = count + 1
			count += 1
			next_pos = (pos[0] + directions[cur_dir][0], pos[1] + directions[cur_dir][1])

			if not (border[0] <= next_pos[0] <= border[2] and border[3] <= next_pos[1] <= border[1]):
				border[(cur_dir-1)%4] += diff[(cur_dir-1)%4]
				cur_dir = (cur_dir+1) % 4
			pos = (pos[0] + directions[cur_dir][0], pos[1] + directions[cur_dir][1])
		return result
        
if __name__ == '__main__':
	sol = Solution()
	print sol.generateMatrix(3)
	print sol.generateMatrix(5)

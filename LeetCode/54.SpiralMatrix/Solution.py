import pdb
class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return []
		row = len(matrix)
		col = len(matrix[0])
		
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
			result.append(matrix[pos[0]][pos[1]])
			count += 1
			next_pos = (pos[0] + directions[cur_dir][0], pos[1] + directions[cur_dir][1])

			if not (border[0] <= next_pos[0] <= border[2] and border[3] <= next_pos[1] <= border[1]):
				border[(cur_dir-1)%4] += diff[(cur_dir-1)%4]
				cur_dir = (cur_dir+1) % 4
			pos = (pos[0] + directions[cur_dir][0], pos[1] + directions[cur_dir][1])
		return result

if __name__ == '__main__':
	sol = Solution()
	matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]] 
	print sol.spiralOrder(matrix)

	matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]] 
	print sol.spiralOrder(matrix)

	matrix = [[1,2], [3,4], [5, 6]]
	print sol.spiralOrder(matrix)

	matrix = [[1,2]]
	print sol.spiralOrder(matrix)

	matrix = [[1,2, 3, 4, 5, 6, 7,8]]
	print sol.spiralOrder(matrix)

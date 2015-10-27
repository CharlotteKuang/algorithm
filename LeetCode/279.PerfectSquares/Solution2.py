from math import sqrt
class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		""" 
		#if sqrt(n) * sqrt(n) == n: return 1

		squares = []
		start  = 1
		while start*start <= n:
			squares.append(start*start)
			start += 1
		
		q = [{'count': 0, 'left': n}]
		visited = {}
		while q:
			cur = q.pop(0)
			if cur['left'] == 0: return cur['count']
			
			count = cur['count']
			left = cur['left']

			for i in squares:
				if i > left: break
				if left-i in visited: continue 
				if i == left: return count + 1
				q.append({'count':count+1, 'left': left-i})
				visited[left-i] = True
		
if __name__ == '__main__':
	sol = Solution()
	for i in range(1, 6000):
		sol.numSquares(i)

#	print sol.numSquares(6024)

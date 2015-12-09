import pdb
class GraphNode:
	def __init__(self):
		self.nbs = []
		self.nbc = 0

class Solution(object):
	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		if n <= 2 and len(edges) <= 2: return [i for i in range(n)]

		graph = {}	

		for edge in edges:
			n1, n2 = edge
			if not n1 in graph:
				graph[n1] = GraphNode()	
			if not n2 in graph:
				graph[n2] = GraphNode()	
			graph[n1].nbs.append(n2)
			graph[n1].nbc += 1
			graph[n2].nbs.append(n1)
			graph[n2].nbc += 1 

		visited = []
		queue = []

		for i in range(n):
			visited.append(False)
			if graph[i].nbc == 1:
				queue.append(i)
				visited[i] = True
		count = len(queue)
		queue.append(-1)

		while True:
			cur = queue.pop(0)

			if cur == -1:
				if count == n: break
				queue.append(-1)
				continue
			for index in graph[cur].nbs:
				graph[index].nbc -= 1
				if not visited[index] and graph[index].nbc == 1:
					queue.append(index)
					visited[index] = True 
					count += 1
			
		return queue

if __name__ == '__main__':
	sol = Solution()
	print sol.findMinHeightTrees(2, [])

	print sol.findMinHeightTrees(12, [[0,1],[0,2],[0,3],[3,4],[3,5],[1,6],[4,7],[2,8],[0,9],[0,10],[2,11]])
	case = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

	print sol.findMinHeightTrees(6, case)

	print sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])

	print sol.findMinHeightTrees(1, []) 

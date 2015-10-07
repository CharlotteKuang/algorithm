import pdb
# Definition for a undirected graph node
class UndirectedGraphNode(object):
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution(object):
	def bfs(self, node):
		visited = {}
		queue = [node]
		visited[node] = True
		while len(queue):	
			cur = queue.pop(0)
			yield cur

			for n in cur.neighbors:
				if not n in visited:
					visited[n] = True
					queue.append(n)

	def cloneGraph(self, node):
		"""
		:type node: UndirectedGraphNode
		:rtype: UndirectedGraphNode
		""" 
		if not node: return

		#create a clone node
		for n in self.bfs(node):
			n.mark = UndirectedGraphNode(n.label)

		rst = node.mark
		#create a clone node
		for n in self.bfs(node):
			for neighbor in n.neighbors:
				n.mark.neighbors.append(neighbor.mark)
				#print neighbor.label
				#print neighbor.mark

		#delete mark
		for n in self.bfs(node):
			del(n.mark)
		return rst 

if __name__ == '__main__':
	sol = Solution()
	n1 = UndirectedGraphNode(1)
	n2 = UndirectedGraphNode(2)
	n3 = UndirectedGraphNode(3)

	n1.neighbors.append(n2)
	n1.neighbors.append(n3)
	n2.neighbors.append(n3)
	n3.neighbors.append(n3)

	rst = sol.cloneGraph(n1)
	for n in sol.bfs(rst):
		print n.label

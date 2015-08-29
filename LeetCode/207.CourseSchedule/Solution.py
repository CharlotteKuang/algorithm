import pdb
class Solution(object):
	def dfs(self, nodes, visited, startNode, nodesSet): 
		#pdb.set_trace()
		visited[startNode] = True
		for pre in nodes[startNode]['list']:
			if not pre in visited: continue
			if pre in nodesSet: return False
			nodesSet[pre] = True
			tmp = self.dfs(nodes, visited, pre, nodesSet)
			if not tmp: return False
			del(nodesSet[pre])
		return True
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		""" 
		#prerequisites.sort(key=lambda x: x[0])
		graphNodes = {}
		for i in range(numCourses):
			graphNodes[i] = {'list': []}
		for pre in prerequisites:
			nodeIdx = pre[0]
			if not pre[1] in graphNodes[nodeIdx]['list']:
				graphNodes[nodeIdx]['list'].append(pre[1])
		#pdb.set_trace()
		#DFS
		visited = {}
		for node in graphNodes:
			if node in visited:
				continue 
			nodesSet = {node: True}
			if not self.dfs(graphNodes, visited, node, nodesSet):
				return False
		return True

if __name__ == '__main__':
	sol = Solution()
	print sol.canFinish(5, [[0,1], [1,2], [0,4], [2,3], [1,3]])
	print sol.canFinish(5, [[0,1], [1,2], [0,4], [2,3], [3,1]])

import pdb

class NFA:
	def __init__(self, count):
		self.count = count
		self.isEnd = False
		self.move = {
			'loop': False
		}

class Solution:
	def constructNFA(self, pattern):
		count = 0
		currentNode = NFA(count) 
		count += 1
		headNode = currentNode 
		for c in pattern:
			newNode = NFA(count)
			count += 1
			if c == '*':
				currentNode.move['loop'] = True 
				currentNode.move['esion'] = newNode
			else:
				currentNode.move[c] = newNode
			currentNode = newNode
		currentNode.isEnd = True
		return headNode

	# @param {string} s
	# @param {string} p
	# @return {boolean}
	def isMatch(self, s, p):
		nfa = self.constructNFA(p)					        
		pdb.set_trace()

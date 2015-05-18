import pdb

class NFA:
	def __init__(self, count):
		self.count = count
		self.isEnd = False
		self.move = {} 
class Solution:
	# @param {string} pattern
	# @return {object}
	def constructNFA(self, pattern):
		i = 0
		stateCount = 0
		startState = NFA(stateCount) 
		curState   = startState
		while i < len(pattern):
			if i+1 < len(pattern) and pattern[i+1] == '*':
				state1 = NFA(stateCount+1)
				state2 = NFA(stateCount+2)
				curState.move['e-closure'] = [state1, state2]
				state1.move[pattern[i]] = [state1]
				state1.move['e-closure'] = [state2]
				curState = state2
				i += 2
				stateCount += 2
			else:
				state = NFA(stateCount+1)
				curState.move[pattern[i]] = [state]
				curState = state
				i += 1
				stateCount += 1
		curState.isEnd = True 
		return {'start': startState, 'count': stateCount}

	def addState(self, state):
		self.newStates.append(state)	
		self.visited[state.count] = True
		if 'e-closure' in state.move:
			for s in state.move['e-closure']:
				if not self.visited[s.count]:
					self.addState(s)
	
	# @param {string} s
	# @param {string} p
	# @return {boolean}
	def isMatch(self, string, p):
		NFAInfo = self.constructNFA(p)
		startState = NFAInfo['start']
		count = NFAInfo['count']
		self.visited = [False]*(count+1)
		#pdb.set_trace()
		self.oldStates = []
		self.newStates = []
		self.addState(startState)
		while len(self.newStates):
			s = self.newStates.pop()
			self.oldStates.append(s)
			self.visited[s.count] = False

		i = 0
		while i < len(string):
			while len(self.oldStates):
				s = self.oldStates.pop()
				if string[i] in s.move:
					for moveState in s.move[string[i]]:
						if not self.visited[moveState.count]:
							self.addState(moveState)
				if '.' in s.move:
					for moveState in s.move['.']:
						if not self.visited[moveState.count]:
							self.addState(moveState)
			while len(self.newStates):
				s = self.newStates.pop()
				self.visited[s.count] = False
				self.oldStates.append(s)
			i += 1
		for s in self.oldStates:
			if s.isEnd: return True
		return False

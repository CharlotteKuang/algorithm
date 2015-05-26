from pdb import set_trace as db

class Solution:
	def recursiveParenthesis(self, ps, tmp, sp, ep):
		if sp == 0 and ep == 0:
			self.result.append(tmp)
			return 
		if len(ps) == 0:
			self.recursiveParenthesis(ps+'(', tmp+'(', sp-1, ep)
		else:
			if ps[-1] == '(':
				self.recursiveParenthesis(ps[:-1], tmp+')', sp, ep-1)
			if sp > 0:
				self.recursiveParenthesis(ps+'(', tmp+'(', sp-1, ep)

	# @param {integer} n
	# @return {string[]}
	def generateParenthesis(self, n):
		self.result = []
		self.recursiveParenthesis('', '', n, n)
		return self.result	

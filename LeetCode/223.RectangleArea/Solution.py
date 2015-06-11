import pdb
class Solution:
	def getDistance(self, a, b, c, d):
		if a > c:
			a, b, c, d = c, d, a, b
		if c < b < d:
			return b - c
		if d <= b:
			return d - c
		return 0

	# @param {integer} A
	# @param {integer} B
	# @param {integer} C
	# @param {integer} D
	# @param {integer} E
	# @param {integer} F
	# @param {integer} G
	# @param {integer} H
	# @return {integer}
	def computeArea(self, A, B, C, D, E, F, G, H):
		total = (C-A)*(D-B) + (G-E)*(H-F)
		width = self.getDistance(A, C, E, G)
		height = self.getDistance(B, D, F, H)
		return total - width * height 

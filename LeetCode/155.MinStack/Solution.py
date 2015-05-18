import pdb

class MinStack:
	def __init__(self):
		self.minInts = []
		self.stack = []

	# @param x, an integer
	# @return an integer
	def push(self, x):
		#pdb.set_trace()
		self.stack.append(x)
		if len(self.minInts) == 0 or  x <= self.minInts[len(self.minInts)-1]:
			self.minInts.append(x)

	# @return nothing
	def pop(self):
		#pdb.set_trace()
		if len(self.stack):
			tmp = self.stack.pop(-1)
			if tmp == self.minInts[-1]: self.minInts.pop(-1)
		else: return None

	# @return an integer
	def top(self):
		if len(self.stack):
			return self.stack[-1]
		else: return None

	# @return an integer
	def getMin(self):
		if len(self.minInts): return self.minInts[-1]
		else: return None 

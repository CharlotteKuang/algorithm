import pdb
class Solution(object):
	def simplifyPath(self, path):
		#pdb.set_trace()
		"""
		:type path: str
		:rtype: str
		""" 
		paths = path.split('/')
		stack = [] 
		result = []
		for p in paths:
			if p:
				if p == '.':
					continue
				elif p == '..':
					if len(result): 
						result.pop() 
				else:
						result.append(p)

		return '/' + '/'.join(result)

if __name__ == '__main__':
	sol = Solution()
	testCases = [
		'//',
		'/home/a/',
		'/home/../',
		'/home/b/./c/../',
		'/../',
		'/home/../',
		'/./'
	]
	for test in testCases:
		print sol.simplifyPath(test)

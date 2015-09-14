import pdb
class Solution(object):
	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		""" 
		count = [1]
		order = []
		for i in range(n):
			count.append((i+1)*count[-1])
			order.append(False)
		result = []
		total = k
		for i in range(n):
			seqSize = count[n-i-1]
			if total > total/seqSize*seqSize:
				idx = total/seqSize+1
			else:
				idx = total/seqSize
			total -= (idx-1)*seqSize
			
			#pdb.set_trace()
			c = 0
			for j in range(n):
				if order[j]: continue
				if c == idx-1:
					result.append(str(j+1))
					order[j] = True 
					break
				else:
					c += 1
		return ''.join(result)
if __name__ == '__main__':
	sol = Solution()
	print sol.getPermutation(3, 1)
	print sol.getPermutation(3, 2)
	print sol.getPermutation(3, 3)
	print sol.getPermutation(3, 4)
	print sol.getPermutation(3, 5)
	print sol.getPermutation(3, 6)

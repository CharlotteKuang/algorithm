import pdb
class Solution(object):
	def mySqrt(self, x):
		if x <= 1: return x
		#pdb.set_trace()
		"""
		:type x: int
		:rtype: int
		""" 
		min_dis = x * x
		head = 1
		tail = x
		result = 1
		while head < tail:
			mid = (head+tail)/2
			dis = x - mid * mid
			if dis < 0:
				tail = mid
			if dis > 0:
				head = mid + 1
			if dis == 0:
				return mid
			if dis > 0 and dis < min_dis:
				result = mid
				min_dis = dis
		return result

if __name__ == '__main__': 
	sol = Solution()
	print sol.mySqrt(14)
	print sol.mySqrt(5)
	print sol.mySqrt(4)
	print sol.mySqrt(9)
	print sol.mySqrt(10)
	print sol.mySqrt(17)
	print sol.mySqrt(1)
	print sol.mySqrt(0)

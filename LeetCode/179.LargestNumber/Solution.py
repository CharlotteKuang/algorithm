class Solution(object):
	def largestNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: str
		""" 
		nums.sort(lambda x,y: int(str(x)+str(y))-int(str(y)+str(x)), reverse=True)
		#print nums
		result = []
		for n in nums:
			result.append(str(n))
		tmp = int(''.join(result))
		return str(tmp)

if __name__ == '__main__':
	sol = Solution()
	test = [3, 30 ,5, 34, 9]
	print sol.largestNumber(test)

	test = [121, 12]
	print sol.largestNumber(test)

	test = [0, 0]
	print sol.largestNumber(test)

	test = [9, 0, 0]
	print sol.largestNumber(test)

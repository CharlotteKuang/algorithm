class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		""" 
		cover = 1
		while cover < n*3: 
			cover *= 3

		count = 0
		q = [1]
		visited = {}
		nums = [1]

		while count < cover:
			cur = q.pop(0)
			for i in [2,3,5]:
				if not cur*i in visited:
					mul = cur*i
					count += 1
					visited[mul] = True
					nums.append(mul)
					q.append(mul)

		nums.sort()
		return nums[n-1]

if __name__ == '__main__': 
	sol = Solution()
	for i in range(1, 1000):
		sol.nthUglyNumber(i)

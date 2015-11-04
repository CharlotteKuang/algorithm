import pdb
class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0

		dp = [1]
		rst = 1
		pdb.set_trace()
		for n in range(1, len(nums)):
			val = 1
			for m in range(len(dp)-1, -1, -1):
				if nums[m] < nums[n]:
					val = max(dp[m]+1, val)
					rst = max(rst, val)
			dp.append(val)
		return rst

if __name__ == '__main__':
	sol = Solution()
	print sol.lengthOfLIS([-2, -1])
	print sol.lengthOfLIS([1,3,6,7,9,4,10,5,6])

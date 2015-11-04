import pdb
class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# The more left and small elements are with higher priority to join the 
		# sub-subsequence
		if not nums: return 0

		def binarySearch(nums, target):
			head, tail = 0, len(nums)-1

			while head < tail:
				mid = (tail+head)/2	
				if target > nums[mid]:
					head = mid+1
				else:
					tail = mid
			return head if target <= nums[head] else head+1

		pdb.set_trace()
		dp = [nums[0]]
		for n in nums[1:]:
			pos = binarySearch(dp, n)
			if pos >= len(dp):
				dp.append(n)
			else:
				dp[pos] = n 
		return len(dp) 

if __name__ == '__main__':
	sol = Solution()
	print sol.lengthOfLIS([-2, -1])
	print sol.lengthOfLIS([10,9,2,5,3,7,101,18])
	print sol.lengthOfLIS([1,3,6,7,9,4,10,5,6])

class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def maxSubArray(self, nums):
		if len(nums) == 0: return 0
			max_ending_here = max_so_far = nums[0]
			# separate the array into serveral segments that end at a position i.
			# These segments have the maximum sum.
			for x in nums[1:]:
				max_ending_here = max(x, max_ending_here + x)
				max_so_far = max(max_so_far, max_ending_here)
		return max_so_far

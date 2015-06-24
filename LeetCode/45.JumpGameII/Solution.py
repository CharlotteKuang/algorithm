class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def jump(self, nums):
		if nums:
			length = len(nums)
			longest = 0
			jumped = [sys.maxint] * length
			jumped[0] = 0
			for i in range(length):
				#start from longest index
				for j in range(longest, min(length,i+nums[i]+1)):
					jumped[j] = min(jumped[j], jumped[i]+1)
				longest = max(longest, i+nums[i])
			return jumped[-1]
		return False

class Solution:
	# @param {integer[]} nums
	# @return {integer[][]}
	def threeSum(self, nums):
		nums.sort()	
		result = []
		length = len(nums)
		for i in range(0, length-2):
			if i > 0 and nums[i] == nums[i-1]: continue
			start = i+1
			end = length-1
			while start < end:
				s = nums[i]+nums[start]+nums[end]
				if s == 0:
					if len(result) > 0 and result[-1][0] == nums[i] and result[-1][1] == nums[start] and result[-1][2] == nums[end]: 
						start += 1
						end -= 1
						continue
					result.append([nums[i], nums[start], nums[end]])
					start += 1
					end -= 1
				elif s > 0: end -= 1
				else: start += 1
		return result

import pdb
class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[][]}
	def fourSum(self, nums, target):
		#pdb.set_trace()
		nums.sort()	
		result = []
		length = len(nums)
		for i in range(0, length-3):
			if i > 0 and nums[i] == nums[i-1]: continue
			for pos in range(i+1, length-2): 
				if pos > i + 1 and nums[pos] == nums[pos-1]: continue
				start = pos+1
				end = length-1
				while start < end:
					s = nums[i]+nums[pos]+nums[start]+nums[end]
					if s == target:
						if len(result) > 0 and result[-1][0] == nums[i] and result[-1][1] == nums[pos] and result[-1][2] == nums[start] and result[-1][3] == nums[end]: 
							start += 1
							end -= 1
							continue
						result.append([nums[i], nums[pos], nums[start], nums[end]])
						start += 1
						end -= 1
					elif s > target: end -= 1
					else: start += 1
		return result
				

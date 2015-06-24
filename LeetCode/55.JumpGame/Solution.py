class Solution:
	# @param {integer[]} nums
	# @return {boolean}
	def canJump(self, nums): 
		if nums:
			length = len(nums)
			longest = 0
			jumped = [False] * length
			jumped[0] = True
			for i in range(length):
				if jumped[i]:
					#start from longest index
					for j in range(longest, i+nums[i]+1):
						if j < length: 
							jumped[j] = True
						else: return True
					longest = max(longest, i+nums[i])
				else:
					break
			return jumped[-1]
		else: return False
